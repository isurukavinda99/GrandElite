import django.views.generic
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from deductions.forms import DeductionsForm
from deductions.models import Deductions

from CAS.decorators import *
from django.contrib.auth.decorators import login_required
decorators = [login_required(login_url='login')  , allowed_users(allowed_roles=['PMS'])]

# Create your views here.
@method_decorator(decorators , name='dispatch')
class DeductionsListView(SuccessMessageMixin, django.views.generic.ListView):
    model = Deductions
    template_name = "deductions/deductions_list.html"
    success_message = "New deduction created successfully"

    # search
    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            objects_list = Deductions.objects.filter(Q(id=query))
            return objects_list
        else:
            objects_list = Deductions.objects.all()
            return objects_list

@method_decorator(decorators , name='dispatch')
class DeductionsCreateView(SuccessMessageMixin, django.views.generic.CreateView):
    model = Deductions
    template_name = "deductions/deductions_form.html"
    success_url = reverse_lazy('deductions:deductions-create')
    form_class = DeductionsForm
    success_message = "New deduction created successfully"


@method_decorator(decorators , name='dispatch')
class DeductionsUpdateView(SuccessMessageMixin, django.views.generic.UpdateView):
    model = Deductions
    template_name = "deductions/deductions_update.html"
    success_url = reverse_lazy('deductions:deductions-list')
    form_class = DeductionsForm
    success_message = "Record was updated successfully"

#
# class DeductionsDeleteView(django.views.generic.DeleteView):
#     model = Deductions
#     template_name = "deductions/deductions_list.html"
#     success_url = reverse_lazy('deductions:deductions-list')


# delete records
@method_decorator(decorators , name='dispatch')
def delete_record(request, pk):
    record = Deductions.objects.get(id=pk)

    if request.method == 'POST':
        print(pk)
        record.delete()
        messages.warning(request, 'Record deleted')

        return HttpResponseRedirect("/deductions")

    return render(request, 'deductions/deductions_list.html', context={})
