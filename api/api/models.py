from django.db import models

# Create your models here.

class Game(models.Model):
    class MaturityRatings(models.TextChoices):
        EVERYONE = 'E', 'Everyone'
        EVERYONE10 = 'E10', 'Everyone 10+'
        TEEN = 'T', 'Teen'
        MATURE17 = 'MATURE17', 'Mature 17+'
        AO = 'AO', 'Adults Only'
        RP = 'RP', 'Rating Pending'
        RP17 = 'RP17', 'Rating Pending (Likely Mature 17+)'
    title = models.TextField(default="Untitled")
    developer = models.TextField(default="Unknown")
    publisher = models.TextField(default="Unknown")
    maturity_rating = models.CharField(
        max_length = 30,
        choices = MaturityRatings.choices,
        default= MaturityRatings.RP
    )
    rating = models.IntegerField(default="1")