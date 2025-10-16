from django.db import models

class Offre(models.Model):
    nom_offre = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    prix_mensuel = models.DecimalField(max_digits=10, decimal_places=2)
    nombre_utilisateurs = models.IntegerField()
    restrictions = models.JSONField(blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.nom_offre

class Entreprise(models.Model):
    nom = models.CharField(max_length=100)
    email_admin = models.EmailField()
    pays = models.CharField(max_length=50, blank=True)
    offre = models.ForeignKey(Offre, on_delete=models.CASCADE)
    abonnement_debut = models.DateField()
    abonnement_fin = models.DateField()
    statut_abonnement = models.CharField(max_length=20, default='actif')
    blocage_total = models.BooleanField(default=False)

    def __str__(self):
        return self.nom

class HistoriqueAbonnement(models.Model):
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    offre = models.ForeignKey(Offre, on_delete=models.CASCADE)
    date_debut = models.DateField()
    date_fin = models.DateField(blank=True, null=True)
    statut = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.entreprise.nom} - {self.offre.nom_offre} ({self.statut})"
