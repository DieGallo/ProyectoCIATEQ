from django.db import models

# Se crea el modelo de la Tabla de api_employee en PostgreSQL
class Employee(models.Model):
    name = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    birthdate = models.DateField(blank=True, null=True)
    sex = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    status = models.BooleanField(default=True)

class Studies(models.Model):
    description =  models.CharField(max_length=400)

class Specialty(models.Model):
    name = models.TextField(max_length=100)

class Student(models.Model):
    name = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    birthdate = models.DateField(blank=True, null=True)
    sex = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    university = models.CharField(max_length=50)
    status = models.BooleanField(default=True)
    startDate = models.DateField(blank=True, null=True)
    endDate = models.DateField(blank=True, null=True)

class Unities(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)

class Area(models.Model):
    name = models.CharField(max_length=100)

class Proyects(models.Model):
    name = models.CharField(max_length=100)
    startDate = models.DateField(blank=True, null=True)
    endDate = models.DateField(blank=True, null=True)

class Events(models.Model):
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    startDate = models.DateField(blank=True, null=True)
    endDate = models.DateField(blank=True, null=True)

class LineInv(models.Model):
    name = models.CharField(max_length=100)

class Articles(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField(blank=True, null=True)

#### Tablas Intermedias ####
# DetProyect - Hace relación con Empleado y Proyectos
class DetProyect(models.Model):
    proyect = models.ForeignKey(Proyects, on_delete=models.CASCADE)
    workers = models.ForeignKey(Employee, on_delete=models.CASCADE)
    students = models.ForeignKey(Student, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

# DetEvent - Hace relación con Empleado y Eventos
class DetEvent(models.Model):
    events = models.ForeignKey(Events, on_delete=models.CASCADE)
    workers = models.ForeignKey(Employee, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    date = models.DateField(blank=True, null=True)

# DetLInvestigation - Hace relación con Empleado y LInvestigación
class DetInvestigation(models.Model):
    workers = models.ForeignKey(Employee, on_delete=models.CASCADE)
    research = models.ForeignKey(LineInv, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

# DetArticle - Hace referencia con Empleado y Articulos
class DetArticle(models.Model):
    workers = models.ForeignKey(Employee, on_delete=models.CASCADE)
    articles = models.ForeignKey(Articles, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)