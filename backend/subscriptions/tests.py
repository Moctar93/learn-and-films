from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from django.contrib.auth.models import User
from .models import UserSubscription, Subscription
# Create your tests here.
class RegisterTestCase(TestCase):
    def setUp(self):
        self.subscription = Subscription.objects.create(
            # Remplissez les champs nécessaires pour créer un abonnement valide
            name='Basic',  # Exemple de champ, adaptez-le à votre modèle
            price=9.99,  # Exemple de prix
            duration_days=30
            # Ajoutez d'autres champs nécessaires selon votre modèle
        )
        
        self.url = '/api/register/'
        self.user_data = {
            
            'user' : { 
                'username': 'jordy',
                'email': 'jordymoukiana@gmail.com',
                'password': '23Aout1996'
            },
            'subscription': self.subscription.id,  # ID d'un abonnement existant
            'start_date': '2024-01-01',
            'end_date': '2024-12-31'
        }

    def test_register(self):
        response = self.client.post(self.url, self.user_data, format='json')

        # Affichez les erreurs si la réponse n'est pas 201
        if response.status_code != status.HTTP_201_CREATED:
            print(response.data)  # Cela affichera les erreurs de validation dans la sortie

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
