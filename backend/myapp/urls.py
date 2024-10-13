from django.urls import path
from .views import home  

urlpatterns = [
    path('', home, name='home'),  # Route pour la page d'accueil
]

