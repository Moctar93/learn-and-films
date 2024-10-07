from django.db import models
from django.contrib.auth.models import User

class Subscription(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    duration_days = models.IntegerField()

    def __str__(self):
        return self.name

class UserSubscription(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    plan = models.CharField(max_length=255
    subscription = models.ForeignKey(Subscription, on_delete=models.SET_NULL, null=True)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()

    def __str__(self):
        return f"{self.user.username} - {self.subscription.name}"

class Transaction(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    transaction_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=50)

