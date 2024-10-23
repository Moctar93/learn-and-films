from django.test import TestCase
from rest_framework import status
from .models import UserSubscription, Subscription
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from django.contrib.auth.models import User

class RegisterTestCase(TestCase):
    def setUp(self):
        # Création d'un abonnement valide pour les tests
        self.subscription = Subscription.objects.create(
            name='Basic',  # Nom de l'abonnement
            price=9.99,    # Prix de l'abonnement
            duration_days=30  # Durée de l'abonnement en jours
        )

        # URL du point de terminaison de l'API de registration
        self.url = '/api/register/'
        
        # Données utilisateur pour la requête POST
        self.user_data = {
            'user': {  # Dictionnaire avec les informations de l'utilisateur
                'username': 'jordy',
                'email': 'jordymoukiana@gmail.com',
                'password': '23Aout1996'
            },
            'subscription': self.subscription.id,  # ID de l'abonnement
            'start_date': '2024-01-01',
            'end_date': '2024-12-31'
        }

    def test_register(self):
        # Envoi d'une requête POST avec les données utilisateur
        response = self.client.post(self.url, self.user_data, format='json')
        
        # Affichez les données de la réponse si le statut n'est pas celui attendu
        if response.status_code != status.HTTP_201_CREATED:
            print("Response Data: ", response.data)
        
        # Vérification que le statut de la réponse est bien HTTP 201 (Créé)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

