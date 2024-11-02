# subscriptions/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('create/<str:plan>/', views.create_subscription, name='create_subscription'),
    path('success/', views.success, name='subscription_success'),
    path('cancel/', views.cancel, name='subscription_cancel'),
]

