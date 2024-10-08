from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import index

router = DefaultRouter()
router.register(r'subscriptions', views.SubscriptionViewSet)
router.register(r'user-subscriptions', views.UserSubscriptionViewSet)
router.register(r'transactions', views.TransactionViewSet)

urlpatterns = [
    path('', index, name='index'),
]

