from rest_framework import serializers
from .models import Offre, Entreprise, HistoriqueAbonnement
from utilisateur.models import Utilisateur
from django.contrib.auth.hashers import make_password
from datetime import date

class OffreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offre
        fields = '__all__'


class EntrepriseSerializer(serializers.ModelSerializer):
    mot_de_passe_admin = serializers.CharField(write_only=True)
    email_admin = serializers.EmailField()

    class Meta:
        model = Entreprise
        fields = [
            'id', 'nom', 'email_admin', 'pays', 'offre',
            'abonnement_debut', 'abonnement_fin',
            'statut_abonnement', 'blocage_total', 'mot_de_passe_admin'
        ]

    def create(self, validated_data):
        mot_de_passe = validated_data.pop('mot_de_passe_admin')
        entreprise = Entreprise.objects.create(**validated_data)

        # 🔹 Création automatique de l'admin associé à cette entreprise
        Utilisateur.objects.create(
            entreprise=entreprise,
            nom_utilisateur=entreprise.email_admin,
            mot_de_passe=make_password(mot_de_passe),
            role='admin',
            email=entreprise.email_admin
        )

        # 🔹 Création automatique de l'historique d'abonnement
        HistoriqueAbonnement.objects.create(
            entreprise=entreprise,
            offre=entreprise.offre,
            date_debut=entreprise.abonnement_debut,
            date_fin=entreprise.abonnement_fin,
            statut=entreprise.statut_abonnement
        )

        return entreprise


class HistoriqueAbonnementSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoriqueAbonnement
        fields = '__all__'
