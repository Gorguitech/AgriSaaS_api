from django.db import models
from abonnement.models import Entreprise

class Membre(models.Model):
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    groupement = models.CharField(max_length=100)
    numero = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)
    sexe = models.CharField(max_length=1)
    localite = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    carte_id = models.CharField(max_length=50)
    part_sociale = models.DecimalField(max_digits=10, decimal_places=2)
    cotisation_annuelle = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Cotisation(models.Model):
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    membre = models.ForeignKey(Membre, on_delete=models.CASCADE)
    annee = models.IntegerField()
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    statut_paiement = models.CharField(max_length=20)

    def __str__(self):
        return f"Cotisation {self.annee} - {self.membre}"
