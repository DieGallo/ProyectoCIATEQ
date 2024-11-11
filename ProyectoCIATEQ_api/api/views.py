# Usamos ambas librerias para poder usar ambos decoradores con la política csrf
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest, JsonResponse
from django.http.response import HttpResponse as HttpResponse
from django.views import View
from .models import Employee
import json

# Declaramos los 4 metodos del CRUD de la API
class EmployeeView(View):
    # Evita la falsicicación de datos acuerdo a CSRF
    # Evita el error 403 Forbidden
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # Devuelve la información de la tabla de datos
    ## Parámetro ID personalizada cada ID para traer los datos de cada empleado
    def get(self, request, id = 0):

        # Condicionales para determinar si se tienen empleados
        ## Lee solamente un sólo empleado
        if(id > 0):
            employees = list(Employee.objects.filter(id=id).values())
            if len(employees) > 0:
                employee = employees[0]
                datos = {'message': "Success", 'employees': employee}
            else:
                datos = {'message': "No one employee found it."}
            return JsonResponse(datos)
        else:
            # Guardamos en una variable el modelo de Employees
            employees = list(Employee.objects.values()) # Se crea con list() para que se pueda serializar
            # Condificón para determinar si tiene algún dato la tabla
            if len(employees) > 0:
                datos = {'message': "Success", 'employees': employees}
            else:
                datos = {'message': "No one employee found it."}

            # Devuelve los datos en formato JSON
            return JsonResponse(datos)

    # Se suben datos a la tabla de nuestra Base de datos
    def post(self, request):
        # print(request.body)
        jd = json.loads(request.body)
        # Convertimos el body en un .create, se agregan todos los campos que tiene el modelo
        Employee.objects.create(name=jd['name'],
                                lastName=jd['lastName'],
                                birthdate=jd['birthdate'],
                                sex=jd['sex'],
                                phone=jd['phone'],
                                email=jd['email'],
                                address=jd['address'],
                                city=jd['city'],
                                country=jd['country'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    # Modifica algún campo o tabla de nuestra Base de datos
    def put(self, request, id):
        jd = json.loads(request.body)
        employees = list(Employee.objects.filter(id=id).values())
        # Condición para actualizar cada uno de los datos del modelo de la tabla Employee
        if len(employees) > 0:
            employee = Employee.objects.get(id=id)
            employee.name = jd['name']
            employee.lastName = jd['lastName']
            employee.birthdate = jd['birthdate']
            employee.sex = jd['sex']
            employee.phone = jd['phone']
            employee.email = jd['email']
            employee.address = jd['address']
            employee.city = jd['city']
            employee.country = jd['country']
            employee.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "No one employee found it for editing."}
        return JsonResponse(datos)

    # Elimina algún campo que contenga la Base de datos
    def delete(self, request, id):
        employees = list(Employee.objects.filter(id=id).values())
        if len(employees) > 0:
            Employee.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "No one employee found it to delete."}
        return JsonResponse(datos)