from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Offre, Entreprise, HistoriqueAbonnement
from .serializers import OffreSerializer, EntrepriseSerializer, HistoriqueAbonnementSerializer
from .permissions import IsEntrepriseAdmin


class OffreViewSet(viewsets.ModelViewSet):
    queryset = Offre.objects.all()
    serializer_class = OffreSerializer


class EntrepriseViewSet(viewsets.ModelViewSet):
    queryset = Entreprise.objects.all()
    serializer_class = EntrepriseSerializer
    authentication_classes = [JWTAuthentication]

    def get_permissions(self):
        """
        🔹 Permet à tout le monde de créer une entreprise (inscription)
        🔹 Mais exige une authentification JWT pour les autres actions
        """
        if self.action == 'create':
            return [AllowAny()]  # création libre
        return [IsAuthenticated(), IsEntrepriseAdmin()]

    def get_queryset(self):
        """
        🔹 Restreint la liste aux entreprises de l'utilisateur connecté
        (utile pour qu’un admin ne voie que sa propre entreprise)
        """
        user = self.request.user
        if hasattr(user, "entreprise"):
            return Entreprise.objects.filter(id=user.entreprise.id)
        return Entreprise.objects.none()


class HistoriqueAbonnementViewSet(viewsets.ModelViewSet):
    queryset = HistoriqueAbonnement.objects.all()
    serializer_class = HistoriqueAbonnementSerializer
