#from django.shortcuts import render
from rest_framework import viewsets
from .models import Offre, Entreprise, HistoriqueAbonnement
from .serializers import OffreSerializer, EntrepriseSerializer, HistoriqueAbonnementSerializer

class OffreViewSet(viewsets.ModelViewSet):
    queryset = Offre.objects.all()
    serializer_class = OffreSerializer

class EntrepriseViewSet(viewsets.ModelViewSet):
    queryset = Entreprise.objects.all()
    serializer_class = EntrepriseSerializer

class HistoriqueAbonnementViewSet(viewsets.ModelViewSet):
    queryset = HistoriqueAbonnement.objects.all()
    serializer_class = HistoriqueAbonnementSerializer
