from django.db import models
from abonnement.models import Entreprise

class Role(models.Model):
    nom = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.nom


class Utilisateur(models.Model):
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    nom_utilisateur = models.CharField(max_length=50, unique=True)
    mot_de_passe = models.CharField(max_length=255)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nom_utilisateur} ({self.role})"
