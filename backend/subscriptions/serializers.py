from rest_framework import serializers
from .models import Subscription, UserSubscription, Transaction, Film
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['id', 'name', 'price', 'duration_days']

class UserSubscriptionSerializer(serializers.ModelSerializer):
    # Récupérer le nom d'utilisateur et l'email de l'utilisateur lié
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = UserSubscription
        fields = ['id', 'username', 'email', 'subscription', 'start_date', 'end_date']

    # Sérialiseur pour la création et mise à jour des utilisateurs
class UserSerializer(serializers.ModelSerializer):
    # On utilise make_password pour hasher le mot de passe lors de la création d'un utilisateur
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        # Hacher le mot de passe avant la création
        validated_data['password'] = make_password(validated_data['password'])
        return super(UserSerializer, self).create(validated_data)

    # Sérialiseur pour les films
class FilmSerializer(serializers.ModelSerializer):
    genre_display = serializers.ReadOnlyField(source='get_genre_display')

    class Meta:
        model = Film
        fields = ['id', 'title', 'genre', 'genre_display', 'release_date', 'duration', 'director', 'description', 'rating']


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
