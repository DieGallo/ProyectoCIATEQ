from django.contrib import admin
from .models import Employees, Areas, Articles, Events, LineInvs, Proyects, Specialties, Students, LevelStudies, Unities

# Registramos el sitio para poder hacer la migracion
admin.site.register(Employees)
admin.site.register(Areas)
admin.site.register(Articles)
admin.site.register(Events)
admin.site.register(LineInvs)
admin.site.register(Proyects)
admin.site.register(Specialties)
admin.site.register(Students)
admin.site.register(LevelStudies)
admin.site.register(Unities)