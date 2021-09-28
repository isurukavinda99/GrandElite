import django_filters

from django_filters import CharFilter

from .models import *

class FilterEmployee(django_filters.FilterSet):

    class Meta:
        model = EmployeeData
        fields = ['id','empStatus','position']

class FilterSalary(django_filters.FilterSet):
    salary_name = CharFilter(field_name='grpCode',lookup_expr='icontains')


    class Meta:
        model = SalaryGroup
        fields = ['grpCode']
        exclude =['grpCode']


class FilterAttRecs(django_filters.FilterSet):

    class Meta:
        model = EmployeeData
        fields = ['id']

class FilterInOutStat(django_filters.FilterSet):

    class Meta:
        model = Attendance
        fields = ['inStatus','outStatus']

