from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets
from .models import Subscription, UserSubscription, Transaction
from .serializers import SubscriptionSerializer, UserSubscriptionSerializer, TransactionSerializer

from django.http import HttpResponse

def index(request):
    return HttpResponse("Page d'accueil")

class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

class UserSubscriptionViewSet(viewsets.ModelViewSet):
    queryset = UserSubscription.objects.all()
    serializer_class = UserSubscriptionSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

