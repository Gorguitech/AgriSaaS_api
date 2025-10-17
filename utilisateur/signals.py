from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Role

@receiver(post_migrate)
def seed_roles(sender, **kwargs):
    if sender.name == "utilisateur":
        roles = [
            ("Admin", "Administrateur de l'entreprise"),
            ("Comptable", "Gère les finances"),
            ("Magasinier", "Gère les entrées et sorties de stock"),
            ("Caissier", "Gère les opérations de caisse"),
            ("Ressource Humaine", "Gère le personnel"),
        ]
        for nom, description in roles:
            Role.objects.get_or_create(nom=nom, defaults={'description': description})
