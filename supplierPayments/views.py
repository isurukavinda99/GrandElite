import django
from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django .urls import reverse


import ISMS.models
import supplierPayments.models

# Create your views here.


# view supplier payments list
class SPaymentsListView(django.views.generic.ListView):
    model = ISMS.models.ConfirmedInvoice.objects.filter(status='pending').all()
    template_name = "sPayments/sPayments_list.html"

    print(model)

    # search
    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            objects_list = ISMS.models.ConfirmedInvoice.objects.filter(Q(status=query))
            return objects_list
        else:
            objects_list = ISMS.models.ConfirmedInvoice.objects.all()
            return objects_list


# view payment (one record)
def view_payment(request,  sk):
    # payment = ISMS.models.ConfirmedInvoice.objects.get(id=rk)
    pendingAll = ISMS.models.ConfirmedInvoice.objects.get(id=sk)
    # single = pendingAll.get(id=sk)

    print(sk)

    context = {
        'object': pendingAll
    }

    return render(request, 'sPayments/sPayments_view.html', context)


def change_status(request, sk):
    payment = ISMS.models.ConfirmedInvoice.objects.get(id=sk)
    payment.status = 'Paid'
    payment.save()

    return HttpResponseRedirect(reverse('supplierPayments:s-payments-list'))