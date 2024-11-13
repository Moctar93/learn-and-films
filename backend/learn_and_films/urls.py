"""
URL configuration for learn_and_films project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from users.homepage import homepage
from django.conf.urls.static import static
from django.conf import settings
from users.views import user_dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('api/', include('subscriptions.urls')),
    path('subscriptions/', include('subscriptions.urls')),
    path('films/', include('films.urls')),
    path('user/dashboard/', user_dashboard, name='user_dashboard'),
    path('', homepage, name='homepage'),  # Page d'accueil
    path('accounts/', include('django.contrib.auth.urls')),  # Ajouter les URL d'authentification par défaut
    #path('register/', views.register, name='register'),  # Appelle la vue d'inscription
    path('', lambda request: redirect('api/users/register/')),  # Redirection vers l'inscription
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
