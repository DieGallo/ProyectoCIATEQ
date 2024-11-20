# Usamos ambas librerias para poder usar ambos decoradores con la política csrf
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import RedirectView
from django.http import JsonResponse
from django.http.response import HttpResponse as HttpResponse
from django.views import View
from .models import Employee, Area, Articles, Events, LineInv, Proyects, Specialty, Student, Studies, Unities
import json

# Vista para la ruta de Urls.py de api
def home(request):
    return render(request, "home.html")

################ API Class Employee ################----
# Declaramos los 4 metodos del CRUD de la API
class EmployeeView(RedirectView):
    # Evita la falsicicación de datos acuerdo a CSRF
    # Evita el error 403 Forbidden
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # Devuelve la información de la tabla de datos
    ## Parámetro ID personalizada cada ID para traer los datos de cada empleado
    def get(self, request, id = 0):
        employees = Employee.objects.all()
        # Condicionales para determinar si se tienen empleados
        ## Lee solamente un sólo empleado
        context = {
            'employees': employees
        }

        return render(request, 'employee.html', context)

    # Se suben datos a la tabla de nuestra Base de datos
    def post(self, request):
        # print(request.body)
        jd = json.loads(request.body)

        try:
            area = Area.objects.get(id=jd['area_id'])
            studies = Studies.objects.get(id=jd['studies_id'])
        except (Area.DoesNotExist, Studies.DoesNotExist):
            return JsonResponse({'message': "Area or Studies not found"}, status=404)

        # Convertimos el body en un .create, se agregan todos los campos que tiene el modelo
        Employee.objects.create(name=jd['name'],
                                lastName=jd['lastName'],
                                birthdate=jd['birthdate'],
                                sex=jd['sex'],
                                phone=jd['phone'],
                                email=jd['email'],
                                address=jd['address'],
                                city=jd['city'],
                                country=jd['country'],
                                area_id=area.id,
                                studies_id=studies.id)
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
            area_id = jd.get('area_id')
            studies_id = jd.get('studies_id')

            if area_id and studies_id is not None:
                try:
                    # Traemos el objeto de Unities(FK) para poder determinar la edición de la variable
                    area = Area.objects.get(id=jd['area_id'])
                    studies = Studies.objects.get(id=jd['studies_id'])
                    employee.area = area
                    employee.studies = studies
                except Unities.DoesNotExist:
                    return JsonResponse({'message': "Area or Studies not found"}, status=404)

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

################ API Class Studies ################----
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

        try:
            specialities = Specialty.objects.get(id=jd['specialty_id'])
        except Unities.DoesNotExist:
            return JsonResponse({'message': "Speciality not found"}, status=404)

        # Convertimos en un objeto la variable
        Studies.objects.create(description=jd['description'],
                               specialty_id=specialities.id)
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        studies = list(Studies.objects.filter(id=id).values())
        if len(studies) > 0:
            study = Studies.objects.get(id=id)
            study.description = jd['description']

            specialty_id = jd.get('specialty_id')

            if specialty_id is not None:
                try:
                    # Traemos el objeto de Specialty(FK) para poder determinar la edición de la variable
                    specialty = Specialty.objects.get(id=specialty_id)
                    study.specialty = specialty
                except Specialty.DoesNotExist:
                    return JsonResponse({'message': "Specialty not found"}, status=404)
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

################ API Class Specialty ################----
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

################ API Class Student ################----
class StudentView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id = 0):
        students = Student.objects.all()
        # Condicionales para determinar si se tienen empleados
        ## Lee solamente un sólo empleado
        context = {
            'students': students
        }

        return render(request, 'students.html', context)

    def post(self, request):
        # Cargamos el cuerpo del request en una variable
        jd = json.loads(request.body)

        try:
            studies = Studies.objects.get(id=jd['studies_id'])
        except Studies.DoesNotExist:
            return JsonResponse({'message': "Studies not found"}, status=404)

        # Convertimos en un objeto la variable
        Student.objects.create(name=jd['name'],
                                lastName=jd['lastName'],
                                birthdate=jd['birthdate'],
                                sex=jd['sex'],
                                phone=jd['phone'],
                                email=jd['email'],
                                address=jd['address'],
                                city=jd['city'],
                                university=jd['university'],
                                startDate=jd['startDate'],
                                studies_id=studies.id)
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
            student.startDate = jd['startDate']
            studies_id = jd.get('studies_id')

            if studies_id is not None:
                try:
                    # Traemos el objeto de Unities(FK) para poder determinar la edición de la variable
                    studies = Studies.objects.get(id=jd['studies_id'])
                    student.studies = studies
                except Unities.DoesNotExist:
                    return JsonResponse({'message': "Studies not found"}, status=404)

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

################ API Class Unities ################----
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

################ API Class Area ################----
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

        # Try-Catch para filtrar los IDs de la tabla
        # Buscamos la instancia de unities
        # Instanciamos en una variable todo el objeto y ponemos el valor del id en el jd
        try:
            unities = Unities.objects.get(id=jd['unities_id'])
        except Unities.DoesNotExist:
            return JsonResponse({'message': "Unities not found"}, status=404)

        # Convertimos en un objeto la variable
        # Se tiene que pasar el .id para que sea el valor de la columna
        Area.objects.create(name=jd['name'],
                            unities_id=unities.id)
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        areas = list(Area.objects.filter(id=id).values())
        if len(areas) > 0:
            area = Area.objects.get(id=id)
            area.name = jd.get('name', area.name)  # Usar el nombre proporcionado o mantener el actual

            # Cada FK de cada tabla se instancia de la siguiente manera.
            unities_id = jd.get('unities_id')

            # Condicional con Try-Catch para verificar si la variable tiene contenido
            if unities_id is not None:
                try:
                    # Traemos el objeto de Unities(FK) para poder determinar la edición de la variable
                    unities = Unities.objects.get(id=unities_id)
                    area.unities = unities
                except Unities.DoesNotExist:
                    return JsonResponse({'message': "Unities not found"}, status=404)

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

################ API Class Proyect ################----
class ProyectView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id = 0):
        proyects = Proyects.objects.all()
        # Condicionales para determinar si se tienen empleados
        ## Lee solamente un sólo empleado
        context = {
            'proyects': proyects
        }

        return render(request, 'proyects.html', context)

    def post(self, request):
        # Cargamos el cuerpo del request en una variable
        jd = json.loads(request.body)

        # Convertimos en un objeto la variable
        Proyects.objects.create(name=jd['name'],
                                startDate=jd['startDate'],
                                endDate=jd['endDate'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        proyects = list(Proyects.objects.filter(id=id).values())
        if len(proyects) > 0:
            proyect = Proyects.objects.get(id=id)
            proyect.name = jd['name']
            proyect.startDate = jd['startDate']
            proyect.endDate = jd['endDate']
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

################ API Class Events ################----
class EventView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id = 0):
        events = Events.objects.all()
        # Condicionales para determinar si se tienen empleados
        ## Lee solamente un sólo empleado
        context = {
            'events': events
        }

        return render(request, 'events.html', context)

    def post(self, request):
        # Cargamos el cuerpo del request en una variable
        jd = json.loads(request.body)

        # Convertimos en un objeto la variable
        Events.objects.create(name=jd['name'],
                                startDate=jd['startDate'],
                                endDate=jd['endDate'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        events = list(Events.objects.filter(id=id).values())
        if len(events) > 0:
            event = Events.objects.get(id=id)
            event.name = jd['name']
            event.startDate = jd['startDate']
            event.endDate = jd['endDate']
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

################ API Class LineInv ################---
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
class ArticlesView(View):
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
        Articles.objects.create(name=jd['name'],
                                date=jd['date'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        articles = list(Articles.objects.filter(id=id).values())
        if len(articles) > 0:
            article = Articles.objects.get(id=id)
            article.name = jd['name']
            article.date = jd['date']
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