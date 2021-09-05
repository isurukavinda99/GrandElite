from django.urls import path

from deductions import views
from deductions.views import DeductionsListView, DeductionsCreateView, DeductionsUpdateView, DeductionsDeleteView


app_name = 'deductions'

urlpatterns = [
    path('', DeductionsListView.as_view(), name='deductions-list'),
    path('create', DeductionsCreateView.as_view(), name='deductions-create'),
    path('update/<int:pk>', DeductionsUpdateView.as_view(), name='deductions-update'),
    path('delete/<int:pk>', DeductionsDeleteView.as_view(), name='deductions-delete'),

    path('deleteDeduction/<int:pk>', views.delete_record, name='deductionDelete'),
]