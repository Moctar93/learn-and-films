# subscriptions/views.py
from django.shortcuts import render, redirect
from django.conf import settings
import paypalrestsdk
from .models import Subscription
from django.contrib.auth.decorators import login_required
import logging

logger = logging.getLogger(__name__)

# Configuration PayPal
paypalrestsdk.configure({
    "mode": settings.PAYPAL_MODE,
    "client_id": settings.PAYPAL_CLIENT_ID,
    "client_secret": settings.PAYPAL_CLIENT_SECRET
})

@login_required
def create_subscription(request, plan):
    # Définir le montant en fonction du plan choisi
    amount = "1.00" if plan == "basic" else "2.00" if plan == "standard" else "3.00"

    # Configurer les informations de paiement pour PayPal
    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal"
        },
        "redirect_urls": {
            "return_url": request.build_absolute_uri('/subscriptions/success/'),
            "cancel_url": request.build_absolute_uri('/subscriptions/cancel/')
        },
        "transactions": [{
            "amount": {
                "total": amount,
                "currency": "USD"
            },
            "description": f"{plan.capitalize()} Subscription"
        }]
    })

    # Création du paiement et redirection vers PayPal pour approbation
    if payment.create():
        for link in payment.links:
            if link.rel == "approval_url":
                return redirect(link.href)
    else:
        return render(request, 'subscriptions/error.html', {"error": payment.error})

@login_required
def success(request):
    # Récupérer les paramètres de requête
    payment_id = request.GET.get('paymentId')
    payer_id = request.GET.get('PayerID')

    logger.info(f"Attempting to verify payment with Payment ID: {payment_id} and Payer ID: {payer_id}")

    # Vérification du paiement auprès de PayPal
    try:
        payment = paypalrestsdk.Payment.find(payment_id)
        if payment.execute({"payer_id": payer_id}):
            # Récupérer l'utilisateur actuel
            user = request.user
            
            # Enregistrement de l'abonnement dans la base de données
            subscription = Subscription.objects.create(user=user, plan=payment.transactions[0].description)

            logger.info(f"Subscription created for user {user.username} with plan {subscription.plan}")

            # Renvoyer la page de succès avec les détails de l'abonnement
            return render(request, 'subscriptions/success.html', {"subscription": subscription})
        else:
            logger.error(f"Payment execution failed: {payment.error}")
            return render(request, 'subscriptions/error.html', {"error": payment.error})
    except Exception as e:
        logger.exception("An error occurred while verifying the payment")
        return render(request, 'subscriptions/error.html', {"error": str(e)})


@login_required
def cancel(request):
    return render(request, 'subscriptions/cancel.html')

