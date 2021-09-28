import django.views.generic
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.decorators import method_decorator

from .forms import AllowancesForm
from .models import Allowances
from CAS.decorators import *
from django.contrib.auth.decorators import login_required
decorators = [login_required(login_url='login')  , allowed_users(allowed_roles=['PMS'])]


# Create your views here.

# list view
@method_decorator(decorators , name='dispatch')
class AllowancesListView(django.views.generic.ListView):
    model = Allowances
    template_name = "allowances/allowances_list.html"

    # search
    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            objects_list = Allowances.objects.filter(Q(id=query))
            return objects_list
        else:
            objects_list = Allowances.objects.all()
            return objects_list


# create view
@method_decorator(decorators , name='dispatch')
class AllowancesCreateView(SuccessMessageMixin, django.views.generic.CreateView):
    model = Allowances
    template_name = "allowances/allowances_form.html"
    success_url = reverse_lazy('allowances:allowances-list')
    form_class = AllowancesForm
    success_message = "New allowance created successfully"


# update view
@method_decorator(decorators , name='dispatch')
class AllowancesUpdateView(SuccessMessageMixin, django.views.generic.UpdateView):
    model = Allowances
    template_name = "allowances/allowances_update.html"
    success_url = reverse_lazy('allowances:allowances-list')
    form_class = AllowancesForm
    success_message = "Record was updated successfully"


# # delete view
# class AllowancesDeleteView(django.views.generic.DeleteView):
#     model = Allowances
#     template_name = "allowances/allowances_list.html"
#     success_url = reverse_lazy('allowances:allowances-list')


# delete records
@method_decorator(decorators , name='dispatch')
def delete_record(request, pk):
    record = Allowances.objects.get(id=pk)

    if request.method == 'POST':
        record.delete()
        messages.warning(request, 'Record deleted')

        return HttpResponseRedirect("/allowances/")

    return render(request, 'allowances/allowances_list.html', context={})
