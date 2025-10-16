from django.contrib import admin

# Register your models here.

from .models import Offre
from .models import Entreprise

admin.site.register(Offre)
admin.site.register(Entreprise)
