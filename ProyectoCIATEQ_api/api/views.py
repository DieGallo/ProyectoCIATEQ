# Usamos ambas librerias para poder usar ambos decoradores con la política csrf
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import RedirectView
from django.http import JsonResponse
from django.http.response import HttpResponse as HttpResponse
from django.views import View
from .models import Employee, Area, Articles, Events, LineInv, Proyects, Specialty, Student, Studies, Unities, DetArticle, DetEvent, DetInvestigation, DetProyect, TypeEvent, TypeProyect, Categories
import json

# Vista para la ruta de Urls.py de api
def home(request):
    return render(request, "home.html")

def form(request):
    return render(request, "addEmployee.html")

################ API Class Employee ################////
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

        # Try-Catch para hacer un llamado de las Foreigns Key de otras tablas.
        try:
            # Instanciamos cada tabla Foránea que tengamos.
            area = Area.objects.get(id=jd['area_id'])
            studies = Studies.objects.get(id=jd['studies_id'])
        except (Area.DoesNotExist, Studies.DoesNotExist):
            # Retornamos una alerta por si da error.
            return JsonResponse({'message': "Area or Studies not found"}, status=404)

        # Convertimos el body en un .create, se agregan todos los campos que tiene el modelo
        # Cada campo de nuestra tabla de la Base de datos tiene que ser llamada para que se guarde.
        Employee.objects.create(name=jd['name'],
                                lastName=jd['lastName'],
                                photo=jd['photo'],
                                birthdate=jd['birthdate'],
                                sex=jd['sex'],
                                phone=jd['phone'],
                                email=jd['email'],
                                address=jd['address'],
                                city=jd['city'],
                                country=jd['country'],
                                startDate=jd['startDate'],
                                area_id=area.id,
                                studies_id=studies.id)
        datos = {'message': "Success"}
        return JsonResponse(datos)

    # Modifica algún campo o tabla de nuestra Base de datos
    def put(self, request, id):
        # Tomamos el cuerpo de nuestros datos y lo pasamos a una variable, estos datos ya están guardados por el POST
        jd = json.loads(request.body)
        # Guardamos en una variable toda la Instancia de la tabla.
        employees = list(Employee.objects.filter(id=id).values())
        # Condición para actualizar cada uno de los datos del modelo de la tabla Employee
        if len(employees) > 0:
            # Ingresamos cada campo de la tabla para que se pueda actualizar.
            employee = Employee.objects.get(id=id)
            employee.name = jd['name']
            employee.lastName = jd['lastName']
            employee.photo = jd['photo']
            employee.birthdate = jd['birthdate']
            employee.sex = jd['sex']
            employee.phone = jd['phone']
            employee.email = jd['email']
            employee.address = jd['address']
            employee.city = jd['city']
            employee.country = jd['country']
            employee.startDate = jd['startDate']
            area_id = jd.get('area_id')
            studies_id = jd.get('studies_id')

            # Condicional para determinar si existen valores en las llaves foráneas.
            if area_id and studies_id is not None:
                try:
                    # Traemos el objeto de Unities(FK) para poder determinar la edición de la variable
                    area = Area.objects.get(id=jd['area_id'])
                    studies = Studies.objects.get(id=jd['studies_id'])
                    employee.area = area
                    employee.studies = studies
                except Area.DoesNotExist or Studies.DoesNotExist:
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

################ API Class Studies #################////
class StudiesView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id = 0):
        studies = Studies.objects.all()
        # Condicionales para determinar si se tienen empleados
        ## Lee solamente un sólo empleado
        context = {
            'studies': studies
        }

        return render(request, 'studies.html', context)

    def post(self, request):
        # Cargamos el cuerpo del request en una variable
        jd = json.loads(request.body)

        try:
            specialities = Specialty.objects.get(id=jd['specialty_id'])
        except Specialty.DoesNotExist:
            return JsonResponse({'message': "Speciality not found"}, status=404)

        # Convertimos en un objeto la variable
        Studies.objects.create(name=jd['name'],
                               specialty_id=specialities.id)
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        studies = list(Studies.objects.filter(id=id).values())
        if len(studies) > 0:
            study = Studies.objects.get(id=id)
            study.name = jd['name']

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

################ API Class Specialty ################////
class SpecialtyView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id = 0):
        specialties = Specialty.objects.all()
        # Condicionales para determinar si se tienen empleados
        ## Lee solamente un sólo empleado
        context = {
            'specialties': specialties
        }

        return render(request, 'specialty.html', context)

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

################ API Class Student ################////
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
                                typeStudent=jd['typeStudent'],
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
            student.typeStudent = jd['typeStudent']
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

################ API Class Unities ################////
class UnitiesView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id = 0):
        unities = Unities.objects.all()
        # Condicionales para determinar si se tienen empleados
        ## Lee solamente un sólo empleado
        context = {
            'unities': unities
        }

        return render(request, 'unities.html', context)

    def post(self, request):
        # Cargamos el cuerpo del request en una variable
        jd = json.loads(request.body)

        # Convertimos en un objeto la variable
        Unities.objects.create(principal=jd['principal'],
                                name=jd['name'],
                                phone=jd['phone'],
                                address=jd['address'],
                                city=jd['city'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        unities = list(Unities.objects.filter(id=id).values())
        if len(unities) > 0:
            unity = Unities.objects.get(id=id)
            unity.principal = jd['principal']
            unity.name = jd['name']
            unity.phone = jd['phone']
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

################ API Class Area ################////
class AreaView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id = 0):
        areas = Area.objects.all()
        # Condicionales para determinar si se tienen empleados
        ## Lee solamente un sólo empleado
        context = {
            'areas': areas
        }

        return render(request, 'areas.html', context)

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
        Area.objects.create(principal=jd['principal'],
                            name=jd['name'],
                            unities_id=unities.id)
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        areas = list(Area.objects.filter(id=id).values())
        if len(areas) > 0:
            area = Area.objects.get(id=id)
            area.principal = jd.get('principal', area.principal)
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

################ API Class Proyect ################////
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

        try:
            typeProyect = TypeProyect.objects.get(id=jd['typeProyect_id'])
        except TypeProyect.DoesNotExist:
            return JsonResponse({'message': "TypeProyect not found"}, status=404)

        # Convertimos en un objeto la variable
        Proyects.objects.create(name=jd['name'],
                                startDate=jd['startDate'],
                                endDate=jd['endDate'],
                                areaKnowledge=jd['areaKnowledge'],
                                place=jd['place'],
                                typeProyect_id=typeProyect.id)
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
            proyect.areaKnowledge = jd['areaKnowledge']
            proyect.place = jd['place']
            typeProyect_id = jd.get('typeProyect_id')

            if typeProyect_id is not None:
                try:
                    # Traemos el objeto de Unities(FK) para poder determinar la edición de la variable
                    typeProyect = TypeProyect.objects.get(id=jd['typeProyect_id'])
                    proyect.typeProyect = typeProyect
                except TypeProyect.DoesNotExist:
                    return JsonResponse({'message': "TypeProyect not found"}, status=404)

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

################ API Class Events ################////
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

        try:
            typeEvent = TypeEvent.objects.get(id=jd['typeEvent_id'])
        except TypeEvent.DoesNotExist:
            return JsonResponse({'message': "TypeEvent not found"}, status=404)

        # Convertimos en un objeto la variable
        Events.objects.create(name=jd['name'],
                                startDate=jd['startDate'],
                                endDate=jd['endDate'],
                                place=jd['place'],
                                typeEvent_id=typeEvent.id)
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
            event.place = jd['place']
            typeEvent_id = jd.get('typeEvent_id')

            if typeEvent_id is not None:
                try:
                    # Traemos el objeto de Unities(FK) para poder determinar la edición de la variable
                    typeEvent = TypeEvent.objects.get(id=jd['typeEvent_id'])
                    event.typeEvent = typeEvent
                except TypeEvent.DoesNotExist:
                    return JsonResponse({'message': "TypeEvent not found"}, status=404)

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

################ API Class LineInv ################////
class LineInvView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id = 0):
        lineinvs = LineInv.objects.all()
        # Condicionales para determinar si se tienen empleados
        ## Lee solamente un sólo empleado
        context = {
            'lineinvs': lineinvs
        }

        return render(request, 'lineinvs.html', context)

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

################ API Class Articles ################////
class ArticlesView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id = 0):
        articles = Articles.objects.all()
        # Condicionales para determinar si se tienen empleados
        ## Lee solamente un sólo empleado
        context = {
            'articles': articles
        }

        return render(request, 'articles.html', context)

    def post(self, request):
        # Cargamos el cuerpo del request en una variable
        jd = json.loads(request.body)

        try:
            category = Categories.objects.get(id=jd['categories_id'])
        except Categories.DoesNotExist:
            return JsonResponse({'message': "Categories not found"}, status=404)

        # Convertimos en un objeto la variable
        Articles.objects.create(name=jd['name'],
                                doi=jd['doi'],
                                url=jd['url'],
                                year=jd['year'],
                                magazine=jd['magazine'],
                                jcr=jd['jcr'],
                                impact=jd['impact'],
                                datePublish=jd['datePublish'],
                                countryPublish=jd['countryPublish'],
                                categories_id=category.id)

        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        articles = list(Articles.objects.filter(id=id).values())
        if len(articles) > 0:
            article = Articles.objects.get(id=id)
            article.name = jd['name']
            article.doi = jd['doi']
            article.url = jd['url']
            article.year = jd['year']
            article.magazine = jd['magazine']
            article.jcr = jd['jcr']
            article.impact = jd['impact']
            article.datePublish = jd['datePublish']
            article.countryPublish = jd['countryPublish']
            categories_id = jd.get('categories_id')

            if categories_id is not None:
                try:
                    # Traemos el objeto de Unities(FK) para poder determinar la edición de la variable
                    categories = Categories.objects.get(id=jd['categories_id'])
                    article.categories = categories
                except Categories.DoesNotExist:
                    return JsonResponse({'message': "Category not found"}, status=404)

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

#### CRUD de las tablas intermedias ####
class DetArticleView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id = 0):
        if(id > 0):
            detarticle = list(DetArticle.objects.filter(id=id).values())
            if len(detarticle) > 0:
                detart = detarticle[0]
                datos = {'message': "Success", 'DetArticles': detart}
            else:
                datos = {'message': "It does not to save data."}
            return JsonResponse(datos)
        else:
            detarticle = list(DetArticle.objects.values())
            if len(detarticle) > 0:
                datos = {'message': "Success", 'DetArticles': detarticle}
            else:
                datos = {'message': "It does not to save data."}
            return JsonResponse(datos)

    def post(self, request):
        jd = json.loads(request.body)

        article = Articles.objects.get(id=jd['articles_id'])
        worker = Employee.objects.get(id=jd['workers_id'])

        DetArticle.objects.create(
            articles_id = article.id,
            workers_id = worker.id
        )

        datos = {'message': 'Success DetArticle'}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        detArticle = DetArticle.objects.get(id=id)

        if 'articles_id' in jd:
            detArticle.articles_id = Articles.objects.get(id=jd['articles_id'])
        if 'workers_id' in jd:
            detArticle.workers_id = Employee.objects.get(id=id['workers_id'])

        detArticle.save()
        datos = {'message': 'Success updated DetArticle'}
        return JsonResponse(datos)

    def delete(self, request, id):
        detArticle = DetArticle.objects.get(id=id)
        detArticle.delete()
        datos = {'message': 'Success deleted DetArticle'}
        return JsonResponse(datos)

#### CRUD de los catálogos de las tablas ####////
class TypeProyectView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id = 0):
        typeproyect = TypeProyect.objects.all()
        # Condicionales para determinar si se tienen empleados
        ## Lee solamente un sólo empleado
        context = {
            'typeproyect': typeproyect
        }

        return render(request, 'typeProyect.html', context)

    def post(self, request):
        jd = json.loads(request.body)
        TypeProyect.objects.create(name=jd['name'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        typeProyect = list(TypeProyect.objects.filter(id=id).values())
        if len(typeProyect) > 0:
            typeProyect = TypeProyect.objects.get(id=id)
            typeProyect.name = jd['name']
            typeProyect.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "There is not an article to save."}
        return JsonResponse(datos)

    def delete(self, request, id = 0):
        typeProyect = list(TypeProyect.objects.filter(id=id).values())
        if len(typeProyect) > 0:
            TypeProyect.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "There is not an article to save."}
        return JsonResponse(datos)

class TypeEventView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id = 0):
        typeevent = TypeEvent.objects.all()
        # Condicionales para determinar si se tienen empleados
        ## Lee solamente un sólo empleado
        context = {
            'typeevent': typeevent
        }

        return render(request, 'typeEvent.html', context)

    def post(self, request):
        jd = json.loads(request.body)
        TypeEvent.objects.create(name=jd['name'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        typeEvent = list(TypeEvent.objects.filter(id=id).values())
        if len(typeEvent) > 0:
            typeEvent = TypeEvent.objects.get(id=id)
            typeEvent.name = jd['name']
            typeEvent.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "There is not an article to save."}
        return JsonResponse(datos)

    def delete(self, request, id = 0):
        typeEvent = list(TypeEvent.objects.filter(id=id).values())
        if len(typeEvent) > 0:
            TypeEvent.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "There is not an article to save."}
        return JsonResponse(datos)

class CategoriesView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id = 0):
        categories = Categories.objects.all()
        # Condicionales para determinar si se tienen empleados
        ## Lee solamente un sólo empleado
        context = {
            'categories': categories
        }

        return render(request, 'categories.html', context)

    def post(self, request):
        jd = json.loads(request.body)
        Categories.objects.create(name=jd['name'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        category = list(Categories.objects.filter(id=id).values())
        if len(category) > 0:
            category = Categories.objects.get(id=id)
            category.name = jd['name']
            category.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "There is not an article to save."}
        return JsonResponse(datos)

    def delete(self, request, id = 0):
        category = list(Categories.objects.filter(id=id).values())
        if len(category) > 0:
            Categories.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "There is not an article to save."}
        return JsonResponse(datos)