# subscriptions/views.py
from django.shortcuts import render, redirect
from django.conf import settings
import paypalrestsdk
from .models import Subscription
from django.contrib.auth.decorators import login_required

paypalrestsdk.configure({
    "mode": settings.PAYPAL_MODE,
    "client_id": settings.PAYPAL_CLIENT_ID,
    "client_secret": settings.PAYPAL_CLIENT_SECRET
})

@login_required
def create_subscription(request, plan):
    # Créez un paiement PayPal
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
                "total": "9.99" if plan == "basic" else "19.99" if plan == "standard" else "29.99",
                "currency": "USD"
            },
            "description": f"{plan.capitalize()} Subscription"
        }]
    })

    if payment.create():
        for link in payment.links:
            if link.rel == "approval_url":
                return redirect(link.href)
    else:
        return render(request, 'subscriptions/error.html', {"error": payment.error}
                )
def success(request):
    # Récupérer l'abonnement, le marquer comme actif, etc.
    return render(request, 'subscriptions/success.html')

def cancel(request):
    return render(request, 'subscriptions/cancel.html')
