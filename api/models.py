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

class Areas(models.Model):
    # Llave foránea de Unities to Areas
    unities = models.ForeignKey(Unities, on_delete=models.CASCADE)
    # Campo agregado
    principal = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    def __str__(self):
        texto = "{0}"
        return texto.format(self.name)

class Specialties(models.Model):
    name = models.TextField(max_length=100)
    # Campo agreado
    estatus = models.BooleanField(default=True)

    def __str__(self):
        texto = "{0}"
        return texto.format(self.name)

class LevelStudies(models.Model):
    # Llave foránea de Studies to Specialty
    specialty = models.ForeignKey(Specialties, on_delete=models.CASCADE)
    name =  models.CharField(max_length=100)

    def __str__(self):
        texto = "{0}"
        return texto.format(self.description)

# Se crea el modelo de la Tabla de api_employee en PostgreSQL
class Employees(models.Model):
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
    area = models.ForeignKey(Areas, on_delete=models.CASCADE)
    studies = models.ForeignKey(LevelStudies, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    # Campos agregados
    startDate = models.DateField(blank=True, null=True)
    endDate = models.DateField(blank=True, null=True)

    # Función para mostrar el dato guardado en Django Admin
    def __str__(self):
        texto = "{0} {1}, ({2})"
        return texto.format(self.name, self.lastName, self.email)

class Students(models.Model):
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
    studies = models.ForeignKey(LevelStudies, on_delete=models.CASCADE)
    # Campo agregado
    typeStudent = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    startDate = models.DateField(blank=True, null=True)
    endDate = models.DateField(blank=True, null=True)

    def __str__(self):
        texto = "{0} {1}, ({2})"
        return texto.format(self.name, self.lastName, self.university)

# Clase agregada
class TypeProyects(models.Model):
    name = models.CharField(max_length=100)

class Proyects(models.Model):
    name = models.CharField(max_length=100)
    startDate = models.DateField(blank=True, null=True)
    endDate = models.DateField(blank=True, null=True)
    # Campos agregados
    areaKnowledge = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    place = models.CharField(max_length=200)
    typeProyect = models.ForeignKey(TypeProyects, on_delete=models.CASCADE)

    def __str__(self):
        texto = "{0}"
        return texto.format(self.name)
# Clase agregada
class TypeEvents(models.Model):
    name = models.CharField(max_length=100)

class Events(models.Model):
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    startDate = models.DateField(blank=True, null=True)
    endDate = models.DateField(blank=True, null=True)
    # Campo agregado
    place = models.CharField(max_length=200)
    typeEvent = models.ForeignKey(TypeEvents, on_delete=models.CASCADE)

    def __str__(self):
        texto = "{0}"
        return texto.format(self.name)

class LineInvs(models.Model):
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
class DetProyects(models.Model):
    proyect = models.ForeignKey(Proyects, on_delete=models.CASCADE)
    workers = models.ForeignKey(Employees, on_delete=models.CASCADE)
    students = models.ForeignKey(Students, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

# DetEvent - Hace relación con Empleado y Eventos
class DetEvents(models.Model):
    events = models.ForeignKey(Events, on_delete=models.CASCADE)
    workers = models.ForeignKey(Employees, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    date = models.DateField(blank=True, null=True)

# DetLInvestigation - Hace relación con Empleado y LInvestigación
class DetInvestigations(models.Model):
    workers = models.ForeignKey(Employees, on_delete=models.CASCADE)
    research = models.ForeignKey(LineInvs, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

# DetArticle - Hace referencia con Empleado y Articulos
class DetArticles(models.Model):
    workers = models.ForeignKey(Employees, on_delete=models.CASCADE)
    articles = models.ForeignKey(Articles, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)