from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from datetime import timedelta, datetime
import uuid

User = get_user_model()

class Subscription(models.Model):
    """
    Modèle représentant les types d'abonnements.
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
    Modèle représentant l'abonnement d'un utilisateur.
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
        Surcharge de la méthode save pour gérer le réabonnement.
        """
        # Vérifier si l'utilisateur a déjà un abonnement actif
        active_subscription = UserSubscription.objects.filter(
            user=self.user,
            end_date__gte=datetime.now()  # Abonnements non expirés
        ).first()

        if active_subscription:
            # Vérifier si l'utilisateur tente de se réabonner à un abonnement de niveau inférieur
            if self.subscription.name < active_subscription.subscription.name:
                raise ValidationError("Vous ne pouvez pas changer à un abonnement de niveau inférieur.")
            else:
                # Conserver les dates d'abonnement existantes
                self.start_date = active_subscription.start_date  # Garder la date de début actuelle
                self.end_date = active_subscription.end_date + self.subscription.get_duration()  # Ajouter la durée de l'abonnement

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
    PAYMENT_METHODS = [
        ('CREDIT_CARD', 'Carte de Crédit'),
        ('PAYPAL', 'PayPal'),
        ('BANK_TRANSFER', 'Virement Bancaire'),
    ]

    STATUS_CHOICES = [
        ('PENDING', 'En attente'),
        ('COMPLETED', 'Complété'),
        ('FAILED', 'Échoué'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Augmenté pour les montants plus élevés
    transaction_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS)  # Corrigé pour ne pas avoir de virgule
    transaction_reference = models.CharField(max_length=100, unique=True)  # Référence unique pour chaque transaction
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')  # Statut de la transaction
    period_start = models.DateTimeField()  # Date de début de la période d'abonnement
    period_end = models.DateTimeField()  # Date de fin de la période d'abonnement

    def __str__(self):
        return f"{self.user.username} a payé {self.amount} pour {self.subscription.name} le {self.transaction_date.strftime('%Y-%m-%d %H:%M:%S')} via {self.get_payment_method_display()} (Statut: {self.get_status_display()})"

