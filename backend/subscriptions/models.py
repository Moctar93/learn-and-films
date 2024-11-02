# subscriptions/models.py
from django.db import models
from django.conf import settings

class Subscription(models.Model):
    BASIC = 'basic'
    STANDARD = 'standard'
    PREMIUM = 'premium'
    SUBSCRIPTION_CHOICES = [
        (BASIC, 'Basic'),
        (STANDARD, 'Standard'),
        (PREMIUM, 'Premium'),
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    plan = models.CharField(max_length=10, choices=SUBSCRIPTION_CHOICES, default=BASIC)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} - {self.plan.capitalize()} Plan"

