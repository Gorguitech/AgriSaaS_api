from django.apps import AppConfig

class UtilisateurConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'utilisateur'

    def ready(self):
        # Import ici pour éviter les imports circulaires
        import utilisateur.signals

