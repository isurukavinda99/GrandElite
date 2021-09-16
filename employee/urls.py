
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path , include
from . import views

urlpatterns = [

    path('', views.dashboard,name="eams-dashboard"),
    path('salary/', views.salary_grp_list,name="eams-salaryList"),
    path('addSalary',views.addSalaryGroup,name ="salaryInsert"),
    path('updateSalary/<str:pk>/',views.updateSal,name ="salaryUpdate"),
    path('generatePdfTest/',views.render_pdf_view, name="testPdf"),
    path('generateUserPdf/<str:pk>/', views.user_render_pdf_view, name="userPdf"),
    path('generateUserList/', views.userList_render_pdf_view, name="userListPdf"),
    path('empListCsv/',views.exportAsCsv,name="csvEmp"),



    path('employees/',views.employee_list,name="eams-empList"),
    path('userProfile/<str:pk>/',views.employee_profile,name="empProfile"),
    path('addEmployee/', views.insertEmployee, name="addEmployee"),
    path('updateEmployee/<str:pk>/', views.updateEmployee, name="updateEmployee"),
    path('deleteSalGrp/<str:pk>/',views.deleteSal, name="deleteSal"),
    path('deleteEmp/<str:pk>/',views.switchEmployee,name="changeEmpStat"),
    path('reallocateEmp/<str:pk>/', views.reallocateEmp, name="realloEmp"),



    ###############Attendance Management System URL #########################
    path('inPortal/', views.inPortal, name="inPortal"),


]



