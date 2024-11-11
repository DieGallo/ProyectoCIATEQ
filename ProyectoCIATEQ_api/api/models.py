from django.db import models

# Se crea el modelo de la Tabla de api_employee en PostgreSQL
class Employee(models.Model):
    name = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    birthdate = models.DateField()
    sex = models.BooleanField()
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)