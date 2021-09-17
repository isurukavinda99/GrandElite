from django.urls import path
from . import views

from allowances.views import AllowancesListView, AllowancesCreateView, AllowancesUpdateView, delete_record

app_name = 'allowances'

urlpatterns = [
    path('', AllowancesListView.as_view(), name='allowances-list'),
    path('create', AllowancesCreateView.as_view(), name='allowances-create'),
    path('update/<int:pk>', AllowancesUpdateView.as_view(), name='allowances-update'),
    path('deleteAllowance/<int:pk>', views.delete_record, name="allowanceDelete"),

]
