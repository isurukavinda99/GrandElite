from django.urls import path

from supplierPayments import views
from supplierPayments.views import SPaymentsListView

app_name = 'supplierPayments'

urlpatterns = [
    path('', SPaymentsListView.as_view(), name='s-payments-list'),

]