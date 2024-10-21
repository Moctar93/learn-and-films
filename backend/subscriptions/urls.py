from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import index
from . import views
from .views import register
from .views import SubscriptionViewSet, UserSubscriptionViewSet, TransactionViewSet, create_checkout_session, payment_success, stripe_webhook

router = DefaultRouter()
router.register(r'subscriptions', views.SubscriptionViewSet)
router.register(r'user-subscriptions', views.UserSubscriptionViewSet)
router.register(r'transactions', views.TransactionViewSet)

urlpatterns = [
    path('', index, name='index'),
     path('api/', include(router.urls)),
      path('register/', register, name='register'),
      path('create-checkout-session/<int:subscription_id>/', create_checkout_session, name='create_checkout_session'),
    path('success/', payment_success, name='payment_success'),
    path('webhook/stripe/', stripe_webhook, name='stripe_webhook'),
]
