from django.urls import path

from employeePayments import views
from employeePayments.views import EPaymentsListView, EPaymentsCreateView, EPaymentsUpdateView, delete_record

app_name = 'employeePayments'

urlpatterns = [
    path('', EPaymentsListView.as_view(), name='e-payments-list'),
    path('create/', EPaymentsCreateView.as_view(), name='e-payments-create'),
    path('update/<int:pk>', EPaymentsUpdateView.as_view(), name='e-payments-update'),
    path('deleteRecord/<int:pk>', views.delete_record, name="deleteRecord"),

    path('findEmployee/', views.employee_find, name="findEmpData"),
    path('calculate/', views.calculate, name="calculate"),


    path('csv/', views.export_csv, name="csv"),
    path('pdf/<int:pk>', views.render_pdf_view, name ="pdf"),

]