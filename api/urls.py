from django.urls import path
from django.views.generic.base import RedirectView
from .views import EmployeeView, AreaView, StudiesView, SpecialtyView, StudentView, UnitiesView, ProyectView, EventView, LineInvView, ArticlesView, DetArticleView, TypeProyectView, TypeEventView, CategoriesView, EmployeeDeleteView, SpecialtyDeleteView
from . import views

urlpatterns = [
    # URL DE LA BIENVENIDA DEL SISTEMA
    path('', views.home, name='home'),

    # Usamos el endpoint para llamar dicha ruta con la vista de Employees
    # Se convierte el archivo EmployeeView a una vista
    # ESTA URL REDIRIJE Y ACTUALIZA LOS DATOS CUANDO SE AGREGA UN EMPLEADO.
    path('employees/', EmployeeView.as_view(), name='employees_list'),

    # Se agrega un int:id para recibir los datos de POST
    # Endpoints del CRUD Back-end.
    path('employees/<int:id>/edit/', EmployeeView.as_view(), name='employees_edit'),
    path('employees/<int:pk>/delete/', EmployeeView.as_view(), name='employees_delete'),

    path('areas/', AreaView.as_view(), name='areas_list'),
    path('areas/<int:id>/edit/', AreaView.as_view(), name='areas_edit'),

    path('studies/', StudiesView.as_view(), name='studies_list'),
    path('studies/<int:id>', StudiesView.as_view(), name='studies_process'),


    path('specialty/', SpecialtyView.as_view(), name='specialty_list'),
    path('specialty/<int:id>/edit/', SpecialtyView.as_view(), name='specialty_edit'),
    path('specialty/<int:pk>/delete/', SpecialtyDeleteView.as_view(), name='specialty_delete'),

    path('students/', StudentView.as_view(), name='students_list'),
    path('students/<int:id>/edit/', StudentView.as_view(), name='students_edit'),

    path('unities/', UnitiesView.as_view(), name='unities_list'),
    path('unities/<int:id>/edit/', UnitiesView.as_view(), name='unities_edit'),

    path('proyects/', ProyectView.as_view(), name='proyects_list'),
    path('proyects/<int:id>', ProyectView.as_view(), name='proyects_process'),

    path('events/', EventView.as_view(), name='events_list'),
    path('events/<int:id>', EventView.as_view(), name='events_process'),

    path('lineinvs/', LineInvView.as_view(), name='lineinvs_list'),
    path('lineinvs/<int:id>/edit/', LineInvView.as_view(), name='lineinvs_edit'),

    path('articles/', ArticlesView.as_view(), name='articles_list'),
    path('articles/<int:id>', ArticlesView.as_view(), name='articles_process'),

    # URLs de tablas intermedias
    path('typeEvent/', TypeEventView.as_view(), name='typeEvent_list'),
    path('typeEvent/<int:id>/edit/', TypeEventView.as_view(), name='typeEvent_edit'),

    path('typeProyect/', TypeProyectView.as_view(), name='typeProyect_list'),
    path('typeProyect/<int:id>/edit/', TypeProyectView.as_view(), name='typeProyect_edit'),

    path('category/', CategoriesView.as_view(), name='category_list'),
    path('category/<int:id>', CategoriesView.as_view(), name='category_process'),
]