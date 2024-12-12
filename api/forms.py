from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'lastName', 'email', 'phone', 'email', 'address', 'city', 'country', 'startDate', 'endDate']
