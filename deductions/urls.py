from django.urls import path

from deductions import views
from deductions.views import DeductionsListView, DeductionsCreateView, DeductionsUpdateView, delete_record


app_name = 'deductions'

urlpatterns = [
    path('', DeductionsListView.as_view(), name='deductions-list'),
    path('create', DeductionsCreateView.as_view(), name='deductions-create'),
    path('update/<int:pk>', DeductionsUpdateView.as_view(), name='deductions-update'),
    path('deleteDeduction/<int:pk>', views.delete_record, name='deductionDelete'),
]