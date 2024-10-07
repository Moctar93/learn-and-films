from django.contrib import admin
from .models import Subscription, UserSubscription, Transaction
from .models import Film

admin.site.register(Subscription)
admin.site.register(UserSubscription)
admin.site.register(Transaction)

class FilmAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'release_date', 'duration', 'rating')
    search_fields = ('title', 'director')
