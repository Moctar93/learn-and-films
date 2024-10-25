from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Subscription, UserSubscription

class RegisterTestCase(APITestCase):
    def setUp(self):
        # Créer une souscription pour les tests
        self.subscription = Subscription.objects.create(
            name="Standard ",
            price= 20,
            duration_days= 30
        )

        # URL de l'API pour l'enregistrement
        self.url = reverse('register')  # Assurez-vous que l'URL est bien configurée dans vos URLs

    def test_register_user_successful(self):
        """Tester l'enregistrement réussi d'un utilisateur et souscription"""
        data = {
            "user": {
                "username": "moctar",
                "email": "moctar@gmail.com",
                "password": "moctarpassword"
            },
            "subscription": self.subscription.id,
            "start_date": "2024-01-01",
            "end_date": "2024-12-31"
        }

        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], "User registered successfully")

        # Vérifie que l'utilisateur a été créé
        user_exists = User.objects.filter(username="moctar").exists()
        self.assertTrue(user_exists)

        # Vérifie que l'abonnement utilisateur a été créé
        user_subscription_exists = UserSubscription.objects.filter(user__username="moctar", subscription=self.subscription).exists()
        self.assertTrue(user_subscription_exists)
