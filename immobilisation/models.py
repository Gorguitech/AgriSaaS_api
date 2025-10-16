from django.db import models
from abonnement.models import Entreprise
from achats.models import Achat
from personnel.models import Personnel

class Immobilisation(models.Model):
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    type_immobilisation = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    date_acquisition = models.DateField()
    valeur_achat = models.DecimalField(max_digits=15, decimal_places=2)
    amortissement_cumule = models.DecimalField(max_digits=15, decimal_places=2)
    valeur_nette = models.DecimalField(max_digits=15, decimal_places=2)
    attribue_a_personnel = models.ForeignKey(Personnel, on_delete=models.SET_NULL, null=True, blank=True)
    statut = models.CharField(max_length=50)
    achat = models.ForeignKey(Achat, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.type_immobilisation} - {self.valeur_nette} F"
