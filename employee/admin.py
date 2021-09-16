from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(SalaryGroup)
admin.site.register(JobRoles)
admin.site.register(EmployeeData)
admin.site.register(Attendance)