import django
from django.db.models import Q
from django.shortcuts import render

# Create your views here.
import supplierPayments.models


class SPaymentsListView(django.views.generic.ListView):
    model = supplierPayments.models.SupplierDetails
    template_name = "sPayments/sPayments_list.html"

    # search
    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            objects_list = supplierPayments.models.SupplierDetails.objects.filter(Q(id=query))
            return objects_list
        else:
            objects_list = supplierPayments.models.SupplierDetails.objects.all()
            return objects_list


#
# def change_status(request, id):
#