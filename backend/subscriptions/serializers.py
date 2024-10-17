from rest_framework import serializers
from .models import Subscription, UserSubscription, Transaction
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'

class UserSubscriptionSerializer(serializers.ModelSerializer):
    # Récupérer le nom d'utilisateur et l'email de l'utilisateur lié
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = UserSubscription
        fields = ['id', 'username', 'email', 'subscription', 'start_date', 'end_date']

    # On surcharge la méthode create pour hasher le mot de passe de l'utilisateur lié
    def create(self, validated_data):
        # Récupérer les données utilisateur
        user_data = validated_data.pop('user', {})
        user_data['password'] = make_password(user_data.get('password'))

        # Créer l'utilisateur associé
        user = User.objects.create(**user_data)

        # Associer l'utilisateur à l'abonnement
        user_subscription = UserSubscription.objects.create(user=user, **validated_data)

        return user_subscription


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
