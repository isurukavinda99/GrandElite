from django.forms import ModelForm
from .models import *
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'


class EmployeeAddForm(ModelForm):
    class Meta:
        model = EmployeeData
        fields = [

            'profile_pic',
            'firstName',
            'lastName',
            'nic',
            'telephone',
            'email',
            'empAdrs',
            'gender',
            'maritalStatus',
            'dob',
            'position',
            'basicSalary'


        ]

        widgets = {
            'dob': DateInput()
        }


class SalaryAddForm(ModelForm):

    class Meta:

        model = SalaryGroup

        fields = [
            'grpCode',
            'grpAmount'


        ]