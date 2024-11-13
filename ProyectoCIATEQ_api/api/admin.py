from django.contrib import admin
from .models import Employee, Area, Articles, Events, LineInv, Proyects, Specialty, Student, Studies, Unities

# Registramos el sitio para poder hacer la migracion
admin.site.register(Employee)
admin.site.register(Area)
admin.site.register(Articles)
admin.site.register(Events)
admin.site.register(LineInv)
admin.site.register(Proyects)
admin.site.register(Specialty)
admin.site.register(Student)
admin.site.register(Studies)
admin.site.register(Unities)