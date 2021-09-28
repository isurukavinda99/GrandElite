import django
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.decorators import method_decorator

import ISMS.models

from CAS.decorators import *
from django.contrib.auth.decorators import login_required
decorators = [login_required(login_url='login')  , allowed_users(allowed_roles=['PMS'])]


# Create your views here.


# view supplier payments list
@method_decorator(decorators , name='dispatch')
class SPaymentsListView(django.views.generic.ListView):
    model = ISMS.models.ConfirmedInvoice.objects.filter(status='pending').all()
    template_name = "sPayments/sPayments_list.html"

    # print(model)

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
@method_decorator(decorators , name='dispatch')
def view_payment(request, sk):
    pendingAll = ISMS.models.ConfirmedInvoice.objects.get(id=sk)

    # print(sk)

    context = {
        'object': pendingAll
    }

    return render(request, 'sPayments/sPayments_view.html', context)


# change payment status
@method_decorator(decorators , name='dispatch')
def change_status(request, pk):
    # if request.method == 'POST':

    payment = ISMS.models.ConfirmedInvoice.objects.get(id=pk)

    payment.status = 'Paid'
    payment.save()
    messages.success(request, 'Payment was done successfully')

    return HttpResponseRedirect(reverse('supplierPayments:s-payments-list'))




