from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import Utilisateur
from django.contrib.auth.hashers import check_password

class CustomTokenObtainPairSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        mot_de_passe = attrs.get('password')

        if not email or not mot_de_passe:
            raise serializers.ValidationError("Email et mot de passe requis")

        try:
            utilisateur = Utilisateur.objects.get(email=email)
        except Utilisateur.DoesNotExist:
            raise serializers.ValidationError("Utilisateur introuvable")

        if not check_password(mot_de_passe, utilisateur.mot_de_passe):
            raise serializers.ValidationError("Mot de passe incorrect")

        # Création du token manuellement
        from rest_framework_simplejwt.tokens import RefreshToken
        token = RefreshToken.for_user(utilisateur)
        token['email'] = utilisateur.email
        token['role'] = utilisateur.role.nom if utilisateur.role else None

        return {
            'refresh': str(token),
            'access': str(token.access_token),
            'user': utilisateur.nom_utilisateur,
            'email': utilisateur.email,
            'role': utilisateur.role.nom if utilisateur.role else None,
        }

class CustomLoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
