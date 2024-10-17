from django.shortcuts import render
from rest_framework.response import Response

from rest_framework import viewsets, status
from .models import Subscription, UserSubscription, Transaction
from .serializers import SubscriptionSerializer, UserSubscriptionSerializer, TransactionSerializer
from rest_framework.decorators import api_view


def index(request):
    return render(request, 'index.html')

class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

class UserSubscriptionViewSet(viewsets.ModelViewSet):
    queryset = UserSubscription.objects.all()
    serializer_class = UserSubscriptionSerializer

@api_view(['POST'])
def register(request):
    serializer = UserSubscriptionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Inscription réussie'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
