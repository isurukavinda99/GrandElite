import django.views.generic
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy

from deductions.forms import DeductionsForm
from deductions.models import Deductions


# Create your views here.


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


class DeductionsCreateView(SuccessMessageMixin, django.views.generic.CreateView):
    model = Deductions
    template_name = "deductions/deductions_form.html"
    success_url = reverse_lazy('deductions:deductions-create')
    form_class = DeductionsForm
    success_message = "New deduction created successfully"


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
def delete_record(request, pk):
    record = Deductions.objects.get(id=pk)

    if request.method == 'POST':
        print(pk)
        record.delete()
        messages.warning(request, 'Record deleted')

        return HttpResponseRedirect("/deductions")

    return render(request, 'deductions/deductions_list.html', context={})
