# users/views.py
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from .serializers import RegisterSerializer, UserSerializer  # Import des deux serializers en une seule ligne
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated

class RegisterView(APIView):
    permission_classes = [AllowAny]  # Permet l'accès sans authentification

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  # Enregistre l'utilisateur
            token, created = Token.objects.get_or_create(user=user)  # Crée un token pour l'utilisateur

            return Response({
                "message": "Utilisateur enregistré avec succès!",
                "data": serializer.data,
                "token": token.key  # Inclut le token dans la réponse
            }, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserListView(APIView):
    permission_classes = [AllowAny]  # IsAuthenticated Remplacer temporairement pour tester

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'username': user.username})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_dashboard(request):
    user = request.user

    # Vérification de l'existence de l'abonnement pour éviter les erreurs
    if hasattr(user, 'subscription'):
        user_data = {
            "name": user.username,
            "email": user.email,
            "subscription_plan": user.subscription.plan,
            "subscription_start": user.subscription.start_date,
            "subscription_end": user.subscription.end_date,
        }
    else:
        user_data = {
            "name": user.username,
            "email": user.email,
            "subscription_plan": None,
            "subscription_start": None,
            "subscription_end": None,
        }

    return Response(user_data)
