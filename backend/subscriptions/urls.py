from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import index, register, genre_list, films_by_genre
from .views import SubscriptionViewSet, UserSubscriptionViewSet, TransactionViewSet, FilmViewSet, create_checkout_session, payment_success, stripe_webhook

router = DefaultRouter()
router.register(r'subscriptions', views.SubscriptionViewSet)
router.register(r'user-subscriptions', views.UserSubscriptionViewSet)
router.register(r'transactions', views.TransactionViewSet)
router.register(r'films', FilmViewSet)

urlpatterns = [
    path('', index, name='index'),
     path('api/', include(router.urls)),
      path('register/', register, name='register'),
       path('genres/', genre_list, name='genre-list'),  # Récupérer tous les genres
       path('films/genre/<str:genre>/', films_by_genre, name='films-by-genre'),  # Films par genre
      path('create-checkout-session/<int:subscription_id>/', create_checkout_session, name='create_checkout_session'),
     path('success/', payment_success, name='payment_success'),
    path('webhook/stripe/', stripe_webhook, name='stripe_webhook'),
]
