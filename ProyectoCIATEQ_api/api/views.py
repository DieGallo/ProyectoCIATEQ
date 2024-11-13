# Usamos ambas librerias para poder usar ambos decoradores con la política csrf
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest, JsonResponse
from django.http.response import HttpResponse as HttpResponse
from django.views import View
from .models import Employee, Area, Articles, Events, LineInv, Proyects, Specialty, Student, Studies, Unities
import json

################ API Class Employee ################
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

################ API Class Studies ################
class StudiesView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id = 0):
        if(id > 0):
            studies = list(Studies.objects.filter(id=id).values())
            if len(studies) > 0:
                study = studies[0]
                datos = {'message': "Success", 'studies': study}
            else:
                datos = {'message': "It does not to save data."}
            return JsonResponse(datos)
        else:
            studies = list(Studies.objects.values())
            if len(studies) > 0:
                datos = {'message': "Success", 'studies': studies}
            else:
                datos = {'message': "It does not to save data."}
            return JsonResponse(datos)

    def post(self, request):
        # Cargamos el cuerpo del request en una variable
        jd = json.loads(request.body)

        # Convertimos en un objeto la variable
        Studies.objects.create(description=jd['description'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        studies = list(Studies.objects.filter(id=id).values())
        if len(studies) > 0:
            study = Studies.objects.get(id=id)
            study.description = jd['description']
            study.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "There is not an study to save."}
        return JsonResponse(datos)

    def delete(self, request, id):
        studies = list(Studies.objects.filter(id=id).values())
        if len(studies) > 0:
            Studies.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "There is not an study to save."}
        return JsonResponse(datos)

################ API Class Specialty ################
class SpecialtyView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id = 0):
        if(id > 0):
            specialties = list(Specialty.objects.filter(id=id).values())
            if len(specialties) > 0:
                specialty = specialties[0]
                datos = {'message': "Success", 'specialties': specialty}
            else:
                datos = {'message': "ID does not exist yet."}
            return JsonResponse(datos)
        else:
            specialties = list(Specialty.objects.values())
            if len(specialties) > 0:
                datos = {'message': "Success", 'specialties': specialties}
            else:
                datos = {'message': "There is not data yet."}
            return JsonResponse(datos)

    def post(self, request):
        # Cargamos el cuerpo del request en una variable
        jd = json.loads(request.body)

        # Convertimos en un objeto la variable
        Specialty.objects.create(name=jd['name'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        specialties = list(Specialty.objects.filter(id=id).values())
        if len(specialties) > 0:
            specialty = Specialty.objects.get(id=id)
            specialty.name = jd['name']
            specialty.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "There is not an specialty to save."}
        return JsonResponse(datos)

    def delete(self, request, id):
        specialties = list(Specialty.objects.filter(id=id).values())
        if len(specialties) > 0:
            Specialty.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "There is not an specialty to save."}
        return JsonResponse(datos)

################ API Class Student ################
class StudentView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id = 0):
        if(id > 0):
            students = list(Student.objects.filter(id=id).values())
            if len(students) > 0:
                student = students[0]
                datos = {'message': "Success", 'students': student}
            else:
                datos = {'message': "ID does not exist yet."}
            return JsonResponse(datos)
        else:
            students = list(Student.objects.values())
            if len(students) > 0:
                datos = {'message': "Success", 'students': students}
            else:
                datos = {'message': "There is not data yet."}
            return JsonResponse(datos)

    def post(self, request):
        # Cargamos el cuerpo del request en una variable
        jd = json.loads(request.body)
        # Convertimos en un objeto la variable
        Student.objects.create(name=jd['name'],
                                lastName=jd['lastName'],
                                birthdate=jd['birthdate'],
                                sex=jd['sex'],
                                phone=jd['phone'],
                                email=jd['email'],
                                address=jd['address'],
                                city=jd['city'],
                                university=jd['university'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        students = list(Student.objects.filter(id=id).values())
        if len(students) > 0:
            student = Student.objects.get(id=id)
            student.name = jd['name']
            student.lastName = jd['lastName']
            student.birthdate = jd['birthdate']
            student.sex = jd['sex']
            student.phone = jd['phone']
            student.email = jd['email']
            student.address = jd['address']
            student.city = jd['city']
            student.university = jd['university']
            student.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "There is not an student to change."}
        return JsonResponse(datos)

    def delete(self, request, id):
        students = list(Student.objects.filter(id=id).values())
        if len(students) > 0:
            Student.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "There is not an student to save."}
        return JsonResponse(datos)

################ API Class Unities ################
class UnitiesView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id = 0):
        if(id > 0):
            unities = list(Unities.objects.filter(id=id).values())
            if len(unities) > 0:
                unity = unities[0]
                datos = {'message': "Success", 'unities': unity}
            else:
                datos = {'message': "ID does not exist yet."}
            return JsonResponse(datos)
        else:
            unities = list(Unities.objects.values())
            if len(unities) > 0:
                datos = {'message': "Success", 'unities': unities}
            else:
                datos = {'message': "There is not data yet."}
            return JsonResponse(datos)

    def post(self, request):
        # Cargamos el cuerpo del request en una variable
        jd = json.loads(request.body)

        # Convertimos en un objeto la variable
        Unities.objects.create(name=jd['name'],
                               address=jd['address'],
                               city=jd['city'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        unities = list(Unities.objects.filter(id=id).values())
        if len(unities) > 0:
            unity = Unities.objects.get(id=id)
            unity.name = jd['name']
            unity.address = jd['address']
            unity.city = jd['city']
            unity.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "There is not an unity to save."}
        return JsonResponse(datos)

    def delete(self, request, id):
        unities = list(Unities.objects.filter(id=id).values())
        if len(unities) > 0:
            Unities.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "There is not an unity to save."}
        return JsonResponse(datos)

################ API Class Area ################
class AreaView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id = 0):
        if(id > 0):
            areas = list(Area.objects.filter(id=id).values())
            if len(areas) > 0:
                area = areas[0]
                datos = {'message': "Success", 'areas': area}
            else:
                datos = {'message': "It does not to save data."}
            return JsonResponse(datos)
        else:
            areas = list(Area.objects.values())
            if len(areas) > 0:
                datos = {'message': "Success", 'areas': areas}
            else:
                datos = {'message': "It does not to save data."}
            return JsonResponse(datos)

    def post(self, request):
        # Cargamos el cuerpo del request en una variable
        jd = json.loads(request.body)

        # Convertimos en un objeto la variable
        Area.objects.create(name=jd['name'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        areas = list(Area.objects.filter(id=id).values())
        if len(areas) > 0:
            area = Area.objects.get(id=id)
            area.name = jd['name']
            area.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "There is not an area to save."}
        return JsonResponse(datos)

    def delete(self, request, id = 0):
        areas = list(Area.objects.filter(id=id).values())
        if len(areas) > 0:
            Area.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "There is not an area to save."}
        return JsonResponse(datos)

################ API Class Proyect ################
class ProyectView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id = 0):
        if(id > 0):
            proyects = list(Proyects.objects.filter(id=id).values())
            if len(proyects) > 0:
                proyect = proyects[0]
                datos = {'message': "Success", 'proyects': proyect}
            else:
                datos = {'message': "It does not to save data."}
            return JsonResponse(datos)
        else:
            proyects = list(Proyects.objects.values())
            if len(proyects) > 0:
                datos = {'message': "Success", 'proyects': proyects}
            else:
                datos = {'message': "It does not to save data."}
            return JsonResponse(datos)

    def post(self, request):
        # Cargamos el cuerpo del request en una variable
        jd = json.loads(request.body)

        # Convertimos en un objeto la variable
        Proyects.objects.create(name=jd['name'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        proyects = list(Proyects.objects.filter(id=id).values())
        if len(proyects) > 0:
            proyect = Proyects.objects.get(id=id)
            proyect.name = jd['name']
            proyect.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "There is not an proyect to save."}
        return JsonResponse(datos)

    def delete(self, request, id = 0):
        proyects = list(Proyects.objects.filter(id=id).values())
        if len(proyects) > 0:
            Proyects.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "There is not an proyect to save."}
        return JsonResponse(datos)

################ API Class Events ################
class EventView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id = 0):
        if(id > 0):
            events = list(Events.objects.filter(id=id).values())
            if len(events) > 0:
                event = events[0]
                datos = {'message': "Success", 'events': event}
            else:
                datos = {'message': "It does not to save data."}
            return JsonResponse(datos)
        else:
            events = list(Events.objects.values())
            if len(events) > 0:
                datos = {'message': "Success", 'events': events}
            else:
                datos = {'message': "It does not to save data."}
            return JsonResponse(datos)

    def post(self, request):
        # Cargamos el cuerpo del request en una variable
        jd = json.loads(request.body)

        # Convertimos en un objeto la variable
        Events.objects.create(name=jd['name'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        events = list(Events.objects.filter(id=id).values())
        if len(events) > 0:
            event = Events.objects.get(id=id)
            event.name = jd['name']
            event.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "There is not an event to save."}
        return JsonResponse(datos)

    def delete(self, request, id = 0):
        events = list(Events.objects.filter(id=id).values())
        if len(events) > 0:
            Events.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "There is not an event to save."}
        return JsonResponse(datos)

################ API Class LineInv ################
class LineInvView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id = 0):
        if(id > 0):
            lineinvs = list(LineInv.objects.filter(id=id).values())
            if len(lineinvs) > 0:
                lineinv = lineinvs[0]
                datos = {'message': "Success", 'lineinvs': lineinv}
            else:
                datos = {'message': "It does not to save data."}
            return JsonResponse(datos)
        else:
            lineinvs = list(LineInv.objects.values())
            if len(lineinvs) > 0:
                datos = {'message': "Success", 'lineinvs': lineinvs}
            else:
                datos = {'message': "It does not to save data."}
            return JsonResponse(datos)

    def post(self, request):
        # Cargamos el cuerpo del request en una variable
        jd = json.loads(request.body)

        # Convertimos en un objeto la variable
        LineInv.objects.create(name=jd['name'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        lineinvs = list(LineInv.objects.filter(id=id).values())
        if len(lineinvs) > 0:
            lineinv = LineInv.objects.get(id=id)
            lineinv.name = jd['name']
            lineinv.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "There is not an lineinv to save."}
        return JsonResponse(datos)

    def delete(self, request, id = 0):
        lineinvs = list(LineInv.objects.filter(id=id).values())
        if len(lineinvs) > 0:
            LineInv.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "There is not an lineinv to save."}
        return JsonResponse(datos)

################ API Class Articles ################
class ArtcilesView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id = 0):
        if(id > 0):
            articles = list(Articles.objects.filter(id=id).values())
            if len(articles) > 0:
                article = articles[0]
                datos = {'message': "Success", 'articles': article}
            else:
                datos = {'message': "It does not to save data."}
            return JsonResponse(datos)
        else:
            articles = list(Articles.objects.values())
            if len(articles) > 0:
                datos = {'message': "Success", 'articles': articles}
            else:
                datos = {'message': "It does not to save data."}
            return JsonResponse(datos)

    def post(self, request):
        # Cargamos el cuerpo del request en una variable
        jd = json.loads(request.body)

        # Convertimos en un objeto la variable
        Articles.objects.create(name=jd['name'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        articles = list(Articles.objects.filter(id=id).values())
        if len(articles) > 0:
            article = Articles.objects.get(id=id)
            article.name = jd['name']
            article.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "There is not an article to save."}
        return JsonResponse(datos)

    def delete(self, request, id = 0):
        articles = list(Articles.objects.filter(id=id).values())
        if len(articles) > 0:
            Articles.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "There is not an article to save."}
        return JsonResponse(datos)