from django.db import models
from abonnement.models import Entreprise

class Banque(models.Model):
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    nom_banque = models.CharField(max_length=100)
    solde = models.DecimalField(max_digits=15, decimal_places=2)

class OperationBancaire(models.Model):
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    banque = models.ForeignKey(Banque, on_delete=models.CASCADE)
    type_operation = models.CharField(max_length=20)
    montant = models.DecimalField(max_digits=15, decimal_places=2)
    date_operation = models.DateField()

class Caisse(models.Model):
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    nom_caisse = models.CharField(max_length=100)
    type_caisse = models.CharField(max_length=50)
    solde = models.DecimalField(max_digits=15, decimal_places=2)

class OperationCaisse(models.Model):
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    caisse = models.ForeignKey(Caisse, on_delete=models.CASCADE)
    type_operation = models.CharField(max_length=20)
    montant = models.DecimalField(max_digits=15, decimal_places=2)
    date_operation = models.DateField()
    description = models.TextField(blank=True)

class EcritureComptable(models.Model):
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    date_ecriture = models.DateField()
    compte_comptable = models.CharField(max_length=50)
    type_ecriture = models.CharField(
        max_length=10,
        choices=[('Débit', 'Débit'), ('Crédit', 'Crédit')]
    )
    montant = models.DecimalField(max_digits=15, decimal_places=2)
    reference = models.CharField(max_length=100, blank=True, null=True)

class InventaireStock(models.Model):
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    produit = models.ForeignKey('achats.Produit', on_delete=models.CASCADE)
    date_inventaire = models.DateField()
    quantite_theorique = models.DecimalField(max_digits=15, decimal_places=2)
    quantite_physique = models.DecimalField(max_digits=15, decimal_places=2)
    ecart = models.DecimalField(max_digits=15, decimal_places=2)
    valorisation_unitaire = models.DecimalField(max_digits=15, decimal_places=2)
    valorisation_totale = models.DecimalField(max_digits=15, decimal_places=2)
    commentaire = models.TextField(blank=True)
class Fournisseur(models.Model):
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    nom_fournisseur = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    dette = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return self.nom_fournisseur
