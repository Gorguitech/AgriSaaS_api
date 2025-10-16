from django.db import models
from abonnement.models import Entreprise

class Utilisateur(models.Model):
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    nom_utilisateur = models.CharField(max_length=50, unique=True)
    mot_de_passe = models.CharField(max_length=255)
    role = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.nom_utilisateur
