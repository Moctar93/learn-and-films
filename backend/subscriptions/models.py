from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta, datetime


User = get_user_model()

class Subscription(models.Model):
    """
    Modèle représentant les types d'abonnements (Basic, Standard, Premium).
    """
    BASIC = 'basic'
    STANDARD = 'standard'
    PREMIUM = 'premium'

    PLAN_CHOICES = [
        (BASIC, 'Basic'),
        (STANDARD, 'Standard'),
        (PREMIUM, 'Premium'),
    ]
    
    name = models.CharField(max_length=100, choices=PLAN_CHOICES, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    duration_days = models.IntegerField(help_text="Durée de l'abonnement en jours")

    def __str__(self):
        return self.get_name_display()

    def get_duration(self):
        """Retourne la durée de l'abonnement sous forme de timedelta."""
        return timedelta(days=self.duration_days)


class UserSubscription(models.Model):
    """
    Modèle représentant l'abonnement d'un utilisateur. Un utilisateur peut se réabonner avant l'expiration
    mais uniquement au même type d'abonnement. Il doit attendre que l'abonnement expire pour changer de type.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subscription = models.ForeignKey(Subscription, on_delete=models.SET_NULL, null=True)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    payment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'subscription'], name='unique_subscription_per_user'),
        ]

    def __str__(self):
        return f"{self.user.username} - {self.subscription.name}"

    def save(self, *args, **kwargs):
        """
        Surcharge de la méthode save pour gérer le réabonnement avant la date d'expiration.
        L'utilisateur ne peut se réabonner que s'il choisit le même type d'abonnement avant la fin.
        S'il veut changer de type, il doit attendre la fin de l'abonnement actuel.
        """
        # Vérifier si l'utilisateur a déjà un abonnement actif
        active_subscription = UserSubscription.objects.filter(
            user=self.user,
            end_date__gte=datetime.now()  # Abonnements non expirés
        ).first()

        for active_subscription:
            # Si l'utilisateur tente de changer d'abonnement avant la fin de l'actuel
            if active_subscription.subscription != self.subscription:
                raise ValueError("Vous ne pouvez pas changer de type d'abonnement avant que l'actuel n'expire.")
            elif:
                # Si l'utilisateur renouvelle le même abonnement avant expiration
                self.start_date = datetime.now()  # Nouvelle date de début
                self.end_date = self.start_date + self.subscription.get_duration()
        else:
            # Si aucun abonnement actif, définir les dates normalement
            self.end_date = self.start_date + self.subscription.get_duration()

        # Sauvegarder le nouvel abonnement
        super(UserSubscription, self).save(*args, **kwargs)

    def is_active(self):
        """Vérifie si l'abonnement est encore valide."""
        return self.end_date >= datetime.now()

class Film(models.Model):
    GENRE_CHOICES = [
        ('action', 'Action'),
        ('comedy', 'Comedy'),
        ('drama', 'Drama'),
        ('horror', 'Horror'),
        ('romance', 'Romance'),
        ('sci-fi', 'Science Fiction'),
        ('thriller', 'Thriller'),
        ('documentary', 'Documentary'),
    ]

    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES)
    release_date = models.DateField(null=True, blank=True)  # Date de sortie
    duration = models.IntegerField(help_text="Durée du film en minutes")  # Durée en minutes
    director = models.CharField(max_length=100, blank=True)  # Réalisateur du film
    description = models.TextField(blank=True)  # Description ou synopsis du film
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)  # Note du film (ex. 8.5)

    def __str__(self):
        return self.title

    def get_genre_display(self):
        """Retourne le nom du genre humainement lisible"""
        return dict(self.GENRE_CHOICES).get(self.genre, 'Unknown')

class Transaction(models.Model):
    """
    Modèle représentant une transaction de paiement.
    """
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    transaction_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=50), choices=[
        ('Credit Card', 'Credit Card'),
        ('PayPal', 'PayPal'),
        ('Bank Transfer', 'Bank Transfer'),
    ])

    def __str__(self):
        return f"Transaction by {self.user.username} on {self.transaction_date} - {self.amount} {self.payment_method}"
