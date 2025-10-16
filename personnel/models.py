from django.db import models
from abonnement.models import Entreprise

class Personnel(models.Model):
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    salaire = models.DecimalField(max_digits=15, decimal_places=2)
    indemnite = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return self.nom

class BulletinPaie(models.Model):
    personnel = models.ForeignKey(Personnel, on_delete=models.CASCADE)
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    date_paie = models.DateField()
    salaire_brut = models.DecimalField(max_digits=15, decimal_places=2)
    retenues = models.DecimalField(max_digits=15, decimal_places=2)
    salaire_net = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f"Paie {self.date_paie} - {self.personnel.nom}"
