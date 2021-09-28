from django.urls import path

from supplierPayments import views
from supplierPayments.views import SPaymentsListView, view_payment, change_status

app_name = 'supplierPayments'

urlpatterns = [
    path('', SPaymentsListView.as_view(), name='s-payments-list'),
    path('pay/<int:sk>', view_payment, name='s-payment'),
    # path('change/<int:pk>', change_status, name='s-change'),
    path('change/<int:pk>', change_status, name='s-change'),


]