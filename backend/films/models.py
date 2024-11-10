# models.py
from django.db import models

class Film(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    video_link = models.URLField()  # Lien vers la vidéo
    image_url = models.URLField()    # URL de l'image d'affiche du film
    release_date = models.DateField()

    def __str__(self):
        return self.title

