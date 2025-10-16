from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import Utilisateur
from django.contrib.auth.hashers import check_password

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    # Indique à SimpleJWT d'utiliser 'email' comme champ d'identification
    username_field = 'email'

    # Redéfinir explicitement les champs que l'on attend
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        token['role'] = user.role
        return token

    def validate(self, attrs):
        email = attrs.get('email')
        mot_de_passe = attrs.get('password')

        if not email or not mot_de_passe:
            raise serializers.ValidationError("Email et mot de passe requis")

        try:
            utilisateur = Utilisateur.objects.get(email=email)
        except Utilisateur.DoesNotExist:
            raise serializers.ValidationError("Utilisateur introuvable")

        # Vérifie le mot de passe haché stocké dans `mot_de_passe`
        if not check_password(mot_de_passe, utilisateur.mot_de_passe):
            raise serializers.ValidationError("Mot de passe incorrect")

        token = self.get_token(utilisateur)
        data = {
            'refresh': str(token),
            'access': str(token.access_token),
            'user': utilisateur.nom_utilisateur,
            'email': utilisateur.email,
            'role': utilisateur.role,
        }
        return data

class CustomLoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
