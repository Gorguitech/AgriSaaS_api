from rest_framework import serializers
from django.db import transaction
from django.core.exceptions import ValidationError
from .models import Offre, Entreprise, HistoriqueAbonnement
from utilisateur.models import Utilisateur, Role
from django.contrib.auth.hashers import make_password


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

    # ✅ Vérifie si un email existe déjà dans la table Utilisateur
    def validate_email_admin(self, value):
        if Utilisateur.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError("Un utilisateur avec cet email existe déjà.")
        if Entreprise.objects.filter(email_admin__iexact=value).exists():
            raise serializers.ValidationError("Une entreprise avec cet email existe déjà.")
        return value

    # ✅ Vérifie les doublons d’entreprise et l’existence de l’offre
    def validate(self, data):
        if Entreprise.objects.filter(nom__iexact=data['nom']).exists():
            raise serializers.ValidationError({"nom": "Une entreprise avec ce nom existe déjà."})
        if not Offre.objects.filter(pk=data.get('offre').pk).exists():
            raise serializers.ValidationError({"offre": "Offre invalide."})
        return data

    def create(self, validated_data):
        mot_de_passe = validated_data.pop('mot_de_passe_admin')

        with transaction.atomic():
            # ✅ Création de l’entreprise
            entreprise = Entreprise.objects.create(**validated_data)

            # ✅ Récupérer ou créer le rôle Admin
            role_admin, _ = Role.objects.get_or_create(
                nom="Admin",
                defaults={"description": "Administrateur de l'entreprise"}
            )

            # ✅ Créer l’utilisateur admin
            Utilisateur.objects.create(
                entreprise=entreprise,
                nom_utilisateur=entreprise.email_admin.split('@')[0],
                mot_de_passe=make_password(mot_de_passe),
                role=role_admin,
                email=entreprise.email_admin
            )

            # ✅ Créer l’historique d’abonnement
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
