from django.contrib import admin

from .models import Citizen, Species

admin.site.register([Citizen, Species])
