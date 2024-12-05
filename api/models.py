from django.db import models

class Unities(models.Model):
    # Campo agreado
    principal = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    # Campo agregado
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)

    def __str__(self):
        texto = "{0} - {1}"
        return texto.format(self.name, self.address)

class Area(models.Model):
    # Llave foránea de Unities to Areas
    unities = models.ForeignKey(Unities, on_delete=models.CASCADE)
    # Campo agregado
    principal = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    def __str__(self):
        texto = "{0}"
        return texto.format(self.name)

class Specialty(models.Model):
    name = models.TextField(max_length=100)
    # Campo agreado
    estatus = models.BooleanField(default=True)

    def __str__(self):
        texto = "{0}"
        return texto.format(self.name)

class Studies(models.Model):
    # Llave foránea de Studies to Specialty
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE)
    name =  models.CharField(max_length=100)

    def __str__(self):
        texto = "{0}"
        return texto.format(self.description)

# Se crea el modelo de la Tabla de api_employee en PostgreSQL
class Employee(models.Model):
    name = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    # Campo agregado
    photo = models.CharField(max_length=300)
    birthdate = models.DateField(blank=True, null=True)
    sex = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    # Llaves Foráneas de la tabla de empleado.
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    studies = models.ForeignKey(Studies, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    # Campos agregados
    startDate = models.DateField(blank=True, null=True)
    endDate = models.DateField(blank=True, null=True)

    # Función para mostrar el dato guardado en Django Admin
    def __str__(self):
        texto = "{0} {1}, ({2})"
        return texto.format(self.name, self.lastName, self.email)

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
    # Llave foránea de Studies a Student
    studies = models.ForeignKey(Studies, on_delete=models.CASCADE)
    # Campo agregado
    typeStudent = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    startDate = models.DateField(blank=True, null=True)
    endDate = models.DateField(blank=True, null=True)

    def __str__(self):
        texto = "{0} {1}, ({2})"
        return texto.format(self.name, self.lastName, self.university)

# Clase agregada
class TypeProyect(models.Model):
    name = models.CharField(max_length=100)

class Proyects(models.Model):
    name = models.CharField(max_length=100)
    startDate = models.DateField(blank=True, null=True)
    endDate = models.DateField(blank=True, null=True)
    # Campos agregados
    areaKnowledge = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    place = models.CharField(max_length=200)
    typeProyect = models.ForeignKey(TypeProyect, on_delete=models.CASCADE)

    def __str__(self):
        texto = "{0}"
        return texto.format(self.name)
# Clase agregada
class TypeEvent(models.Model):
    name = models.CharField(max_length=100)

class Events(models.Model):
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    startDate = models.DateField(blank=True, null=True)
    endDate = models.DateField(blank=True, null=True)
    # Campo agregado
    place = models.CharField(max_length=200)
    typeEvent = models.ForeignKey(TypeEvent, on_delete=models.CASCADE)

    def __str__(self):
        texto = "{0}"
        return texto.format(self.name)

class LineInv(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        texto = "{0}"
        return texto.format(self.name)
# Clase agregada
class Categories(models.Model):
    name = models.CharField(max_length=100)

class Articles(models.Model):
    name = models.CharField(max_length=100)
    # Campos agreados
    doi = models.CharField(max_length=50)
    url = models.CharField(max_length=150)
    year = models.CharField(max_length=10)
    magazine = models.CharField(max_length=100)
    jcr = models.BooleanField(default=False)
    impact = models.CharField(max_length=200)
    datePublish = models.DateField(blank=True, null=True)
    countryPublish = models.CharField(max_length=50)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)

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