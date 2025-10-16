from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OffreViewSet, EntrepriseViewSet, HistoriqueAbonnementViewSet

router = DefaultRouter()
router.register(r'offres', OffreViewSet)
router.register(r'entreprises', EntrepriseViewSet)
router.register(r'historiques', HistoriqueAbonnementViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
