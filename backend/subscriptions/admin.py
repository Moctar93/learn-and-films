from django.contrib import admin
from .models import Subscription, UserSubscription, Transaction

admin.site.register(Subscription)
admin.site.register(UserSubscription)
admin.site.register(Transaction)
