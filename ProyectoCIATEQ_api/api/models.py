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

    # Función para mostrar el dato guardado en Django Admin
    def __str__(self):
        texto = "{0} {1}, ({2})"
        return texto.format(self.name, self.lastName, self.email)

class Studies(models.Model):
    description =  models.CharField(max_length=400)

    def __str__(self):
        texto = "{0}"
        return texto.format(self.description)
class Specialty(models.Model):
    name = models.TextField(max_length=100)

    def __str__(self):
        texto = "{0}"
        return texto.format(self.name)
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

    def __str__(self):
        texto = "{0} {1}, ({2})"
        return texto.format(self.name, self.lastName, self.university)

class Unities(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)

    def __str__(self):
        texto = "{0} - {1}"
        return texto.format(self.name, self.address)

class Area(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        texto = "{0}"
        return texto.format(self.name)

class Proyects(models.Model):
    name = models.CharField(max_length=100)
    startDate = models.DateField(blank=True, null=True)
    endDate = models.DateField(blank=True, null=True)

    def __str__(self):
        texto = "{0}"
        return texto.format(self.name)

class Events(models.Model):
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    startDate = models.DateField(blank=True, null=True)
    endDate = models.DateField(blank=True, null=True)

    def __str__(self):
        texto = "{0}"
        return texto.format(self.name)
class LineInv(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        texto = "{0}"
        return texto.format(self.name)

class Articles(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField(blank=True, null=True)

    def __str__(self):
        texto = "{0} - {1}"
        return texto.format(self.name, self.date)

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