from django.db import models
from abonnement.models import Entreprise

class UniteMesure(models.Model):
    nom_unite = models.CharField(max_length=50, unique=True)

class Produit(models.Model):
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    nom_produit = models.CharField(max_length=100)
    type_produit = models.CharField(max_length=50)
    quantite_stock = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    unite = models.ForeignKey(UniteMesure, on_delete=models.CASCADE)

class Achat(models.Model):
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    fournisseur = models.ForeignKey('finances.Fournisseur', on_delete=models.CASCADE)
    date_achat = models.DateField()
    montant_total_HT = models.DecimalField(max_digits=15, decimal_places=2)
    montant_total_TVA = models.DecimalField(max_digits=15, decimal_places=2)
    montant_total_TTC = models.DecimalField(max_digits=15, decimal_places=2)
    etat = models.CharField(max_length=50)
    provenance_fonds = models.CharField(max_length=20)
    type_achat = models.CharField(max_length=50)
    description = models.TextField(blank=True)

class AchatProduit(models.Model):
    achat = models.ForeignKey(Achat, on_delete=models.CASCADE, related_name='produits')
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.DecimalField(max_digits=15, decimal_places=2)
    prix_unitaire_HT = models.DecimalField(max_digits=15, decimal_places=2)
    montant_TVA = models.DecimalField(max_digits=15, decimal_places=2)
    montant_TTC = models.DecimalField(max_digits=15, decimal_places=2)
