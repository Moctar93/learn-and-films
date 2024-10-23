from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
import stripe
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from rest_framework import viewsets, status
from .models import Subscription, UserSubscription, Transaction, Film
from .serializers import SubscriptionSerializer, UserSubscriptionSerializer, TransactionSerializer, FilmSerializer
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from datetime import datetime

# Initialiser la clé API Stripe
stripe.api_key = settings.STRIPE_SECRET_KEY


def index(request):
    return render(request, 'index.html')

def genre_list(request):
# Votre logique pour récupérer et afficher les genres
    genres = [...]  # Remplacez par la logique appropriée
    return render(request, 'genre_list.html', {'genres': genres})

def films_by_genre(request, genre):
    # Vérifie que le genre passé dans l'URL est valide
    genre_choices = dict(Film.GENRE_CHOICES).keys()
    if genre.lower() not in genre_choices:
        message = f"Le genre '{genre}' n'est pas valide."
        return render(request, 'films_by_genre.html', {'films': [], 'genre': genre, 'message': message})
    
    # Récupérer les films filtrés par genre (insensible à la casse)
    films = Film.objects.filter(genre__iexact=genre)  # iexact = ignore la casse

    # Si aucun film n'est trouvé, affiche un message
    if not films:
        message = f"Aucun film trouvé pour le genre {genre}."
    else:
        message = None
    
    return render(request, 'films_by_genre.html', {'films': films, 'genre': genre, 'message': message})

class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer


# VueSet pour gérer les abonnements des utilisateurs
class UserSubscriptionViewSet(viewsets.ModelViewSet):
    queryset = UserSubscription.objects.all()
    serializer_class = UserSubscriptionSerializer

class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

# Vue pour enregistrer un nouvel abonnement utilisateur
@api_view(['POST'])
def register(request):
    user_data = request.data.get('user')  # Récupération des données utilisateur
    subscription_id = request.data.get('subscription')

    if not user_data or not isinstance(user_data, dict):
        return Response({'error': 'Invalid user data format'}, status=status.HTTP_400_BAD_REQUEST)

    if not subscription_id:
        return Response({'error': 'Subscription ID is required'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        # Créer l'utilisateur
        user = User.objects.create_user(
            username=user_data['username'],
            email=user_data['email'],
            password=user_data['password']
        )

        # Récupérer la souscription
        subscription = Subscription.objects.get(id=subscription_id)

        # Créer la souscription utilisateur
        user_subscription = UserSubscription.objects.create(
            user=user,
            subscription=subscription,
            start_date=request.data['start_date'],
            end_date=request.data['end_date']
        )

        return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)

    except Subscription.DoesNotExist:
        return Response({'error': 'Subscription does not exist'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

# Vue pour créer une session de paiement Stripe
@api_view(['POST'])
def create_checkout_session(request, subscription_id):
    try:
        # Récupérer l'abonnement sélectionné
        subscription = get_object_or_404(Subscription, id=subscription_id)

        # Créer une session de paiement Stripe
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': subscription.name,
                    },
                    'unit_amount': int(subscription.price * 100),  # Stripe attend des montants en centimes
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=request.build_absolute_uri('/success/') + '?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=request.build_absolute_uri('/cancel/'),
        )

        # Retourner l'ID de la session pour la redirection vers Stripe Checkout
        return JsonResponse({'id': session.id})
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


# Vue pour afficher le succès du paiement
@api_view(['GET'])
def payment_success(request):
    session_id = request.GET.get('session_id')
    try:
        session = stripe.checkout.Session.retrieve(session_id)

        if session.payment_status == 'paid':
            # Récupérer les informations de l'utilisateur et de l'abonnement
            user = request.user
            subscription_name = session['display_items'][0]['custom']['name']
            subscription = Subscription.objects.get(name=subscription_name)

            # Créer une transaction
            transaction = Transaction.objects.create(
                user=user,
                subscription=subscription,
                amount=session.amount_total / 100,  # Convertir en dollars
                payment_method=session.payment_method_types[0],
                transaction_reference=session.id,
                status='COMPLETED',
                period_start=datetime.now(),
                period_end=datetime.now() + subscription.get_duration()
            )

            # Créer un abonnement pour l'utilisateur
            UserSubscription.objects.create(
                user=user,
                subscription=subscription,
                email=user.email,
                start_date=transaction.period_start,
                end_date=transaction.period_end
            )

            return Response({'message': 'Paiement réussi et abonnement activé.'})
        else:
            return Response({'error': 'Le paiement n\'a pas été complété.'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


# Webhook pour traiter les événements de Stripe
@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')
    event = None

    try:
        # Vérifier la signature du webhook
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        # Mauvais payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Mauvaise signature
        return HttpResponse(status=400)

    # Gérer l'événement de paiement réussi
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']

        # Récupérer les informations d'abonnement et de l'utilisateur
        user_id = session['client_reference_id']  # Assurez-vous de stocker cet identifiant
        subscription_name = session['display_items'][0]['custom']['name']
        user = User.objects.get(id=user_id)
        subscription = Subscription.objects.get(name=subscription_name)

        # Créer la transaction et l'abonnement utilisateur
        transaction = Transaction.objects.create(
            user=user,
            subscription=subscription,
            amount=session['amount_total'] / 100,  # Montant en dollars
            payment_method=session['payment_method_types'][0],
            transaction_reference=session['id'],
            status='COMPLETED',
            period_start=datetime.now(),
            period_end=datetime.now() + subscription.get_duration()
        )

        # Activer l'abonnement utilisateur
        UserSubscription.objects.create(
            user=user,
            subscription=subscription,
            email=user.email,
            start_date=transaction.period_start,
            end_date=transaction.period_end
        )

    return HttpResponse(status=200)
