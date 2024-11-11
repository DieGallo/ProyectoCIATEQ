from django.contrib import admin
from .models import Employee

# Registramos el sitio para poder hacer la migracion
admin.site.register(Employee)