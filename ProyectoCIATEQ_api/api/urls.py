from django.urls import path
from .views import EmployeeView, AreaView, StudiesView, SpecialtyView, StudentView, UnitiesView, ProyectView, EventView, LineInvView, ArticlesView

urlpatterns = [
    # Usamos el endpoint para llamar dicha ruta con la vista de Employees
    # Se convierte el archivo EmployeeView a una vista
    path('employees/', EmployeeView.as_view(), name='employees_list'),
    # Se agrega un int:id para recibir los datos de POST
    path('employees/<int:id>', EmployeeView.as_view(), name='employees_process'),
    path('area/', AreaView.as_view(), name='area_list'),
    path('area/<int:id>', AreaView.as_view(), name='area_process'),
    path('studies/', StudiesView.as_view(), name='studies_list'),
    path('studies/<int:id>', StudiesView.as_view(), name='studies_process'),
    path('specialty/', SpecialtyView.as_view(), name='specialty_list'),
    path('specialty/<int:id>', SpecialtyView.as_view(), name='specialty_process'),
    path('student/', StudentView.as_view(), name='student_list'),
    path('student/<int:id>', StudentView.as_view(), name='student_process'),
    path('unities/', UnitiesView.as_view(), name='unities_list'),
    path('unities/<int:id>', UnitiesView.as_view(), name='unities_process'),
    path('proyects/', ProyectView.as_view(), name='proyects_list'),
    path('proyects/<int:id>', ProyectView.as_view(), name='proyects_process'),
    path('events/', EventView.as_view(), name='events_list'),
    path('events/<int:id>', EventView.as_view(), name='events_process'),
    path('lineinvs/', LineInvView.as_view(), name='lineinvs_list'),
    path('lineinvs/<int:id>', LineInvView.as_view(), name='lineinvs_process'),
    path('articles/', ArticlesView.as_view(), name='articles_list'),
    path('articles/<int:id>', ArticlesView.as_view(), name='articles_process'),
]