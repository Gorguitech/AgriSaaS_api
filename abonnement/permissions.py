from rest_framework.permissions import BasePermission

class IsEntrepriseAdmin(BasePermission):
    """
    Permission pour n'autoriser que les utilisateurs admin de l'entreprise.
    """

    def has_object_permission(self, request, view, obj):
        # On vérifie que l'utilisateur appartient à la même entreprise ET est admin
        return (
            hasattr(request.user, 'entreprise') and
            obj.entreprise == request.user.entreprise and
            request.user.role == "admin"
        )
