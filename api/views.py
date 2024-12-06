# Usamos ambas librerias para poder usar ambos decoradores con la política csrf
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import RedirectView
from django.http import JsonResponse
from django.http.response import HttpResponse as HttpResponse
from django.views import View
from .models import Employees, Areas, Articles, Events, LineInvs, Proyects, Specialties, Students, LevelStudies, Unities, DetArticles, DetEvents, DetInvestigations, DetProyects, TypeEvents, TypeProyects, Categories
import json
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

# Vista para la ruta de Urls.py de api
def home(request):
    return render(request, "home.html")

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
        employees = Employees.objects.all()
        employee = get_object_or_404(Employees, id=id) if id else None

        # Cuando se tienen FK se tienen que instaciar los datos en get para los combobox
        area = Areas.objects.all()
        studies = LevelStudies.objects.all()

        # Condicionales para determinar si se tienen empleados
        ## Lee solamente un sólo empleado
        context = {
            'employees': employees,
            'employee': employee,

            # Traemos los datos de las FK
            # Cuando se recarge la página el dato aparezca los combobox
            'areas': area,
            'studies': studies,
        }

        # Retornamos la vista principal de la Tabla.
        return render(request, 'employees/employee.html', context)

    # Se suben datos a la tabla de nuestra Base de datos
    def post(self, request, id=0):
        name = request.POST.get('name')
        lastName = request.POST.get('lastName')
        photo = request.POST.get('photo')
        birthdate = request.POST.get('birthdate')
        sex = request.POST.get('sex')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        city = request.POST.get('city')
        country = request.POST.get('country')
        startDate = request.POST.get('startDate')
        endDate = request.POST.get('endDate')
        area_id = request.POST.get('area_id')
        studies_id = request.POST.get('studies_id')

        if id:
            return self.put(request, id)
        else:
            try:
                # Instanciamos cada tabla Foránea que tengamos.
                area = Areas.objects.get(id=area_id)
                studies = LevelStudies.objects.get(id=studies_id)
            except (Areas.DoesNotExist, LevelStudies.DoesNotExist):
                # Retornamos una alerta por si da error.
                return JsonResponse({'message': "Area or Studies not found"}, status=404)

            Employees.objects.create(
                name=name,
                lastName=lastName,
                photo=photo,
                birthdate=birthdate,
                sex=sex,
                phone=phone,
                email=email,
                address=address,
                city=city,
                country=country,
                startDate=startDate,
                endDate=endDate,
                area=area,  # Asignar instancia del área
                studies=studies  # Asignar instancia del nivel de estudios
            )
        return redirect('/employees/')

    # Modifica algún campo o tabla de nuestra Base de datos
    def put(self, request, id):
        employee = get_object_or_404(Employees, id=id)

        name = request.POST.get('name')
        lastName = request.POST.get('lastName')
        photo = request.POST.get('photo')
        birthdate = request.POST.get('birthdate')
        sex = request.POST.get('sex')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        city = request.POST.get('city')
        country = request.POST.get('country')
        startDate = request.POST.get('startDate')
        endDate = request.POST.get('endDate')
        area_id = request.POST.get('area_id')
        studies_id = request.POST.get('studies_id')

        # Intentar obtener las FK solo si se proporcionan nuevas IDs
        area = None
        studies = None
        if area_id:
            area = get_object_or_404(Areas, id=area_id)
        if studies_id:
            studies = get_object_or_404(LevelStudies, id=studies_id)

        if name: employee.name = name
        if lastName: employee.lastName = lastName
        if photo: employee.photo = photo
        if birthdate: employee.birthdate = birthdate
        if sex: employee.sex = sex
        if phone: employee.phone = phone
        if email: employee.email = email
        if address: employee.address = address
        if city: employee.city = city
        if country: employee.country = country
        if startDate: employee.startDate = startDate
        if endDate: employee.endDate = endDate
        if area: employee.area = area
        if studies: employee.studies = studies

        employee.save()
        return redirect('/employees/')

class EmployeeDeleteView(DeleteView):
    model = Employees
    employees = Employees.objects.all()
    success_url = reverse_lazy('employees_list')
    template_name = 'employees/employee.html'


################ API Class Studies #################////
class StudiesView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id = 0):
        studies = LevelStudies.objects.all()
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
            specialities = Specialties.objects.get(id=jd['specialty_id'])
        except Specialties.DoesNotExist:
            return JsonResponse({'message': "Speciality not found"}, status=404)

        # Convertimos en un objeto la variable
        LevelStudies.objects.create(name=jd['name'],
                               specialty_id=specialities.id)
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = request.PUT
        studies = list(LevelStudies.objects.filter(id=id).values())
        if len(studies) > 0:
            study = LevelStudies.objects.get(id=id)
            study.name = jd['name']

            specialty_id = jd.get('specialty_id')

            if specialty_id is not None:
                try:
                    # Traemos el objeto de Specialty(FK) para poder determinar la edición de la variable
                    specialty = Specialties.objects.get(id=specialty_id)
                    study.specialty = specialty
                except Specialties.DoesNotExist:
                    return JsonResponse({'message': "Specialty not found"}, status=404)
            study.save()
        return redirect('/specialty/')

    def delete(self, request, id):
        studies = list(LevelStudies.objects.filter(id=id).values())
        if len(studies) > 0:
            LevelStudies.objects.filter(id=id).delete()
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
        specialties = Specialties.objects.all()
        specialty = get_object_or_404(Specialties, id=id) if id else None

        # Condicionales para determinar si se tienen empleados
        ## Lee solamente un sólo empleado
        context = {
            'specialties': specialties, # GET
            'specialty': specialty # PUT
        }

        return render(request, 'specialties/specialty.html', context)

    def post(self, request, id=0):
        name = request.POST.get('name')
        if id:
            return self.put(request, id)
        else:
            Specialties.objects.create(name=name)
            return redirect('/specialty/')

    def put(self, request, id):
        specialty = get_object_or_404(Specialties, id=id)
        name = request.POST.get('name')
        if name:
            specialty.name = name
            specialty.save()
        return redirect('/specialty/')

class SpecialtyDeleteView(DeleteView):
    model = Specialties
    specialties = Specialties.objects.all()
    success_url = reverse_lazy('specialty_list')
    template_name = 'specialties/specialty.html'

################ API Class Student ################////
class StudentView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id = 0):
        students = Students.objects.all()
        student = get_object_or_404(Students, id=id) if id else None

        studies = LevelStudies.objects.all()
        # Condicionales para determinar si se tienen empleados
        ## Lee solamente un sólo empleado
        context = {
            'students': students, # GET
            'student': student, # PUT
            'studies': studies, # FK
        }

        return render(request, 'students/students.html', context)

    def post(self, request, id=0):
        name = request.POST.get('name')
        lastName = request.POST.get('lastName')
        birthdate = request.POST.get('birthdate')
        sex = request.POST.get('sex')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        city = request.POST.get('city')
        university = request.POST.get('university')
        typeStudent = request.POST.get('typeStudent')
        startDate = request.POST.get('startDate')
        endDate = request.POST.get('endDate')
        studies_id = request.POST.get('studies_id')

        if id:
            return self.put(request, id)
        else:
            try:
                # Instanciamos cada tabla Foránea que tengamos.
                studies = LevelStudies.objects.get(id=studies_id)
            except LevelStudies.DoesNotExist:
                # Retornamos una alerta por si da error.
                return JsonResponse({'message': "Studies not found"}, status=404)

            # Convertimos en un objeto la variable
            Students.objects.create(
                name=name,
                lastName=lastName,
                birthdate=birthdate,
                sex=sex,
                phone=phone,
                email=email,
                address=address,
                city=city,
                university=university,
                typeStudent=typeStudent,
                startDate=startDate,
                endDate=endDate,
                studies=studies
            )
        return redirect('/students/')

    def put(self, request, id):
        student = get_object_or_404(Students, id=id)

        name = request.POST.get('name')
        lastName = request.POST.get('lastName')
        birthdate = request.POST.get('birthdate')
        sex = request.POST.get('sex')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        city = request.POST.get('city')
        university = request.POST.get('university')
        typeStudent = request.POST.get('typeStudent')
        startDate = request.POST.get('startDate')
        endDate = request.POST.get('endDate')
        studies_id = request.POST.get('studies_id')

        studies = None
        if studies_id:
            studies = get_object_or_404(LevelStudies, id=studies_id)

        if name: student.name = name
        if lastName: student.lastName = lastName
        if birthdate: student.birthdate = birthdate
        if sex: student.sex = sex
        if phone: student.phone = phone
        if email: student.email = email
        if address: student.address = address
        if city: student.city = city
        if university: student.university = university
        if typeStudent: student.typeStudent = typeStudent
        if startDate: student.startDate = startDate
        if endDate: student.endDate = endDate
        if studies: student.studies = studies
        student.save()
        return redirect('/students/')

    def delete(self, request, id):
        students = list(Students.objects.filter(id=id).values())
        if len(students) > 0:
            Students.objects.filter(id=id).delete()
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
        unity = get_object_or_404(Unities, id=id) if id else None
        # Condicionales para determinar si se tienen empleados
        ## Lee solamente un sólo empleado
        context = {
            'unities': unities,
            'unity': unity # PUT
        }

        return render(request, 'unities/unities.html', context)

    def post(self, request, id=0):
        # Cargamos el cuerpo del request en una variable
        principal = request.POST.get('principal')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        city = request.POST.get('city')

        if id:
            return self.put(request, id)
        else:
            # Convertimos en un objeto la variable
            Unities.objects.create(principal=principal,
                                name=name,
                                phone=phone,
                                address=address,
                                city=city)
            return redirect('/unities/')

    def put(self, request, id):
        unity = get_object_or_404(Unities, id=id)
        principal = request.POST.get('principal')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        city = request.POST.get('city')

        if principal and name and phone and address and city:
            unity.principal = principal
            unity.name = name
            unity.phone = phone
            unity.address = address
            unity.city = city
            unity.save()
        return redirect('/unities/')

    # def delete(self, request, id):
    #     unities = list(Unities.objects.filter(id=id).values())
    #     if len(unities) > 0:
    #         Unities.objects.filter(id=id).delete()
    #         datos = {'message': "Success"}
    #     else:
    #         datos = {'message': "There is not an unity to save."}
    #     return JsonResponse(datos)

################ API Class Area ################////
class AreaView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id = 0):
        areas = Areas.objects.all()
        unities = Unities.objects.all()
        # Condicionales para determinar si se tienen empleados
        ## Lee solamente un sólo empleado
        context = {
            'areas': areas,
            'unities': unities,
        }

        return render(request, 'areas/areas.html', context)

    def post(self, request):
        # Cargamos el cuerpo del request en una variable
        jd = request.POST

        # Try-Catch para filtrar los IDs de la tabla
        # Buscamos la instancia de unities
        # Instanciamos en una variable todo el objeto y ponemos el valor del id en el jd
        try:
            unities = Unities.objects.get(id=jd['unities_id'])
        except Unities.DoesNotExist:
            return JsonResponse({'message': "Unities not found"}, status=404)

        # Convertimos en un objeto la variable
        # Se tiene que pasar el .id para que sea el valor de la columna
        Areas.objects.create(principal=jd['principal'],
                            name=jd['name'],
                            unities_id=unities.id)
        return redirect('/areas/')

    # def put(self, request, id):
    #     jd = json.loads(request.body)
    #     areas = list(Area.objects.filter(id=id).values())
    #     if len(areas) > 0:
    #         area = Area.objects.get(id=id)
    #         area.principal = jd.get('principal', area.principal)
    #         area.name = jd.get('name', area.name)  # Usar el nombre proporcionado o mantener el actual
    #         # Cada FK de cada tabla se instancia de la siguiente manera.
    #         unities_id = jd.get('unities_id')

    #         # Condicional con Try-Catch para verificar si la variable tiene contenido
    #         if unities_id is not None:
    #             try:
    #                 # Traemos el objeto de Unities(FK) para poder determinar la edición de la variable
    #                 unities = Unities.objects.get(id=unities_id)
    #                 area.unities = unities
    #             except Unities.DoesNotExist:
    #                 return JsonResponse({'message': "Unities not found"}, status=404)

    #         area.save()
    #         datos = {'message': "Success"}
    #     else:
    #         datos = {'message': "There is not an area to save."}
    #     return JsonResponse(datos)

    def delete(self, request, id = 0):
        areas = list(Areas.objects.filter(id=id).values())
        if len(areas) > 0:
            Areas.objects.filter(id=id).delete()
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
        typeP = TypeProyects.objects.all()
        # Condicionales para determinar si se tienen empleados
        ## Lee solamente un sólo empleado
        context = {
            'proyects': proyects,
            'typeProyect': typeP,
        }

        return render(request, 'proyects/proyects.html', context)

    def post(self, request):
        # Cargamos el cuerpo del request en una variable
        jd = request.POST

        try:
            typeProyect = TypeProyects.objects.get(id=jd['typeProyect_id'])
        except TypeProyects.DoesNotExist:
            return JsonResponse({'message': "TypeProyect not found"}, status=404)

        # Convertimos en un objeto la variable
        Proyects.objects.create(name=jd['name'],
                                startDate=jd['startDate'],
                                endDate=jd['endDate'],
                                areaKnowledge=jd['areaKnowledge'],
                                place=jd['place'],
                                typeProyect_id=typeProyect.id)
        return redirect('/proyects/')

    # def put(self, request, id):
    #     jd = json.loads(request.body)
    #     proyects = list(Proyects.objects.filter(id=id).values())
    #     if len(proyects) > 0:
    #         proyect = Proyects.objects.get(id=id)
    #         proyect.name = jd['name']
    #         proyect.startDate = jd['startDate']
    #         proyect.endDate = jd['endDate']
    #         proyect.areaKnowledge = jd['areaKnowledge']
    #         proyect.place = jd['place']
    #         typeProyect_id = jd.get('typeProyect_id')

    #         if typeProyect_id is not None:
    #             try:
    #                 # Traemos el objeto de Unities(FK) para poder determinar la edición de la variable
    #                 typeProyect = TypeProyect.objects.get(id=jd['typeProyect_id'])
    #                 proyect.typeProyect = typeProyect
    #             except TypeProyect.DoesNotExist:
    #                 return JsonResponse({'message': "TypeProyect not found"}, status=404)

    #         proyect.save()
    #         datos = {'message': "Success"}
    #     else:
    #         datos = {'message': "There is not an proyect to save."}
    #     return JsonResponse(datos)

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
        typeE = TypeEvents.objects.all()
        # Condicionales para determinar si se tienen empleados
        ## Lee solamente un sólo empleado
        context = {
            'events': events,
            'typeEvent': typeE,
        }

        return render(request, 'events/events.html', context)

    def post(self, request):
        # Cargamos el cuerpo del request en una variable
        jd = request.POST

        try:
            typeEvent = TypeEvents.objects.get(id=jd['typeEvent_id'])
        except TypeEvents.DoesNotExist:
            return JsonResponse({'message': "TypeEvent not found"}, status=404)

        # Convertimos en un objeto la variable
        Events.objects.create(name=jd['name'],
                                startDate=jd['startDate'],
                                endDate=jd['endDate'],
                                place=jd['place'],
                                typeEvent_id=typeEvent.id)
        return redirect('/events/')

    # def put(self, request, id):
    #     jd = json.loads(request.body)
    #     events = list(Events.objects.filter(id=id).values())
    #     if len(events) > 0:
    #         event = Events.objects.get(id=id)
    #         event.name = jd['name']
    #         event.startDate = jd['startDate']
    #         event.endDate = jd['endDate']
    #         event.place = jd['place']
    #         typeEvent_id = jd.get('typeEvent_id')

    #         if typeEvent_id is not None:
    #             try:
    #                 # Traemos el objeto de Unities(FK) para poder determinar la edición de la variable
    #                 typeEvent = TypeEvent.objects.get(id=jd['typeEvent_id'])
    #                 event.typeEvent = typeEvent
    #             except TypeEvent.DoesNotExist:
    #                 return JsonResponse({'message': "TypeEvent not found"}, status=404)

    #         event.save()
    #         datos = {'message': "Success"}
    #     else:
    #         datos = {'message': "There is not an event to save."}
    #     return JsonResponse(datos)

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
        lineinvs = LineInvs.objects.all()
        lineinv = get_object_or_404(LineInvs, id=id) if id else None

        # Condicionales para determinar si se tienen empleados
        ## Lee solamente un sólo empleado
        context = {
            'lineinvs': lineinvs,
            'lineinv': lineinv
        }

        return render(request, 'lineinvs/lineinvs.html', context)

    def post(self, request, id=0):
        # Cargamos el cuerpo del request en una variable
        name = request.POST.get('name')
        if id:
            return self.put(request, id)
        else:
            LineInvs.objects.create(name=name)
            return redirect('/lineinvs/')

    def put(self, request, id):
        lineinv = get_object_or_404(LineInvs, id=id)
        name = request.POST.get('name')
        if name:
            lineinv.name = name
            lineinv.save()
        return redirect('/lineinvs/')

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
            detarticle = list(DetArticles.objects.filter(id=id).values())
            if len(detarticle) > 0:
                detart = detarticle[0]
                datos = {'message': "Success", 'DetArticles': detart}
            else:
                datos = {'message': "It does not to save data."}
            return JsonResponse(datos)
        else:
            detarticle = list(DetArticles.objects.values())
            if len(detarticle) > 0:
                datos = {'message': "Success", 'DetArticles': detarticle}
            else:
                datos = {'message': "It does not to save data."}
            return JsonResponse(datos)

    def post(self, request):
        jd = json.loads(request.body)

        article = Articles.objects.get(id=jd['articles_id'])
        worker = Employees.objects.get(id=jd['workers_id'])

        DetArticles.objects.create(
            articles_id = article.id,
            workers_id = worker.id
        )

        datos = {'message': 'Success DetArticle'}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        detArticle = DetArticles.objects.get(id=id)

        if 'articles_id' in jd:
            detArticle.articles_id = Articles.objects.get(id=jd['articles_id'])
        if 'workers_id' in jd:
            detArticle.workers_id = Employees.objects.get(id=id['workers_id'])

        detArticle.save()
        datos = {'message': 'Success updated DetArticle'}
        return JsonResponse(datos)

    def delete(self, request, id):
        detArticle = DetArticles.objects.get(id=id)
        detArticle.delete()
        datos = {'message': 'Success deleted DetArticle'}
        return JsonResponse(datos)

#### CRUD de los catálogos de las tablas ####////
class TypeProyectView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id = 0):
        typeproyects = TypeProyects.objects.all()
        typeproyect = get_object_or_404(TypeProyects, id=id) if id else None
        # Condicionales para determinar si se tienen empleados
        ## Lee solamente un sólo empleado
        context = {
            'typeproyects': typeproyects,
            'typeproyect': typeproyect
        }

        return render(request, 'typeProyect/typeProyect.html', context)

    def post(self, request, id=0):
        name = request.POST.get('name')
        if id:
            return self.put(request, id)
        else:
            TypeProyects.objects.create(name=name)
            return redirect('/typeProyect/')

    def put(self, request, id):
        typeP = get_object_or_404(TypeProyects, id=id)
        name = request.POST.get('name')
        if name:
            typeP.name = name
            typeP.save()
        return redirect('/typeProyect/')

    # def delete(self, request, id = 0):
    #     typeProyect = list(TypeProyect.objects.filter(id=id).values())
    #     if len(typeProyect) > 0:
    #         TypeProyect.objects.filter(id=id).delete()
    #         datos = {'message': "Success"}
    #     else:
    #         datos = {'message': "There is not an article to save."}
    #     return JsonResponse(datos)

class TypeEventView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id = 0):
        typeevents = TypeEvents.objects.all()
        typeevent = get_object_or_404(TypeEvents, id=id) if id else None
        # Condicionales para determinar si se tienen empleados
        ## Lee solamente un sólo empleado
        context = {
            'typeevents': typeevents,
            'typeevent': typeevent
        }

        return render(request, 'typeEvent/typeEvent.html', context)

    def post(self, request, id=0):
        name = request.POST.get('name')
        if id:
            return self.put(request, id)
        else:
            TypeEvents.objects.create(name=name)
            return redirect('/typeEvent/')

    def put(self, request, id):
        typeE = get_object_or_404(TypeEvents, id=id)
        name = request.POST.get('name')
        if name:
            typeE.name = name
            typeE.save()
        return redirect('/typeEvent/')

    # def delete(self, request, id = 0):
    #     typeEvent = list(TypeEvent.objects.filter(id=id).values())
    #     if len(typeEvent) > 0:
    #         TypeEvent.objects.filter(id=id).delete()
    #         datos = {'message': "Success"}
    #     else:
    #         datos = {'message': "There is not an article to save."}
    #     return JsonResponse(datos)

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