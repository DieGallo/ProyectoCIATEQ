from django.urls import path
from .views import EmployeeView

urlpatterns = [
    # Usamos el endpoint para llamar dicha ruta con la vista de Employees
    # Se convierte el archivo EmployeeView a una vista
    path('employees/', EmployeeView.as_view(), name='employees_list'),
    # Se agrega un int:id para recibir los datos de POST
    path('employees/<int:id>', EmployeeView.as_view(), name='employees_process'),
]