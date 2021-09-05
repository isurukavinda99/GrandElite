import django.views.generic
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy

from deductions.forms import DeductionsForm
from deductions.models import Deductions


# Create your views here.


class DeductionsListView(django.views.generic.ListView):
    model = Deductions
    template_name = "deductions/deductions_list.html"

    # search
    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            objects_list = Deductions.objects.filter(Q(id=query))
            return objects_list
        else:
            objects_list = Deductions.objects.all()
            return objects_list


class DeductionsCreateView(django.views.generic.CreateView):
    model = Deductions
    template_name = "deductions/deductions_form.html"
    success_url = reverse_lazy('deductions:deductions-create')
    form_class = DeductionsForm


class DeductionsUpdateView(django.views.generic.UpdateView):
    model = Deductions
    template_name = "deductions/deductions_update.html"
    success_url = reverse_lazy('deductions:deductions-list')
    form_class = DeductionsForm


class DeductionsDeleteView(django.views.generic.DeleteView):
    model = Deductions
    template_name = "deductions/deductions_list.html"
    success_url = reverse_lazy('deductions:deductions-list')


# delete records
def delete_record(request, pk):
    record = Deductions.objects.get(id=pk)

    if request.method == 'POST':
        print(pk)
        record.delete()

        return HttpResponseRedirect("/deductions")

    return render(request, 'deductions/deductions_list.html', context={})
