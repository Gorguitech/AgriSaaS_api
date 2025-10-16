from django.db import models
from abonnement.models import Entreprise
from achats.models import Produit

class Client(models.Model):
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    nom_client = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)

    def __str__(self):
        return self.nom_client

class Vente(models.Model):
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.IntegerField()
    montant_HT = models.DecimalField(max_digits=15, decimal_places=2)
    montant_TVA = models.DecimalField(max_digits=15, decimal_places=2)
    montant_TTC = models.DecimalField(max_digits=15, decimal_places=2)
    date_vente = models.DateField()
    provenance_fonds = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.produit.nom_produit} x{self.quantite} > {self.client.nom_client}"
