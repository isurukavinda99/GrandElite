from django.forms import ModelForm
from .models import *


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'


class PaymentForm(ModelForm):
    class Meta:
        model = PaySlip
        fields = ['month', 'allowance', 'deduction']
