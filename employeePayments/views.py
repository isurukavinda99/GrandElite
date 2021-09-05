from django.core.exceptions import MultipleObjectsReturned
from django.db.models import Q
import django.views.generic
from django.http import HttpResponseRedirect, HttpResponse


from django.urls import reverse_lazy, reverse
import csv
from django.shortcuts import render, get_object_or_404
from django.views import View

from allowances.models import Allowances
from deductions.models import Deductions
from employeePayments.forms import PaymentForm
from employeePayments.models import *



from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


# Create your views here.

# list view
class EPaymentsListView(django.views.generic.ListView):
    model = PaySlip
    template_name = "ePayments/ePayments_list.html"

    # search
    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            objects_list = PaySlip.objects.filter(Q(empID=query))
            return objects_list
        else:
            objects_list = PaySlip.objects.all()
            return objects_list


# create view
class EPaymentsCreateView(django.views.generic.CreateView):
    model = PaySlip
    template_name = "ePayments/ePayments_form.html"
    success_url = reverse_lazy('employeePayments:e-payments-list')
    form_class = PaymentForm


# update view
class EPaymentsUpdateView(django.views.generic.UpdateView):
    model = PaySlip
    template_name = "ePayments/ePayments_update.html"
    success_url = reverse_lazy('employeePayments:e-payments-list')
    form_class = PaymentForm


# delete view
class EPaymentsDeleteView(django.views.generic.DeleteView):
    model = PaySlip
    template_name = " "
    success_url = reverse_lazy('employeePayments:e-payments-list')


# delete records
def delete_record(request, pk):
    record = PaySlip.objects.get(id=pk)

    if request.method == 'POST':
        record.delete()

        return HttpResponseRedirect("/pms/")

    return render(request, 'ePayments/ePayments_list.html', context={})


#####################################################################################################################

# pdf generation
def render_pdf_view(request,pk):
    payslipData = PaySlip.objects.get(id=pk)
    template_path = 'ePayments/paySlip.html'
    context = {'ps':payslipData}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="paySlip.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

#########################################################################################################


# csv generation
def export_csv(request):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['Emp ID', 'Emp Name', 'Basic wage', 'Allowance', 'Deduction', 'Net pay'])

    for p in PaySlip.objects.all().values_list('empID', 'empName', 'basicWage', 'allowance', 'deduction', 'netPay'):
        writer.writerow(p)

    response['Content-Disposition'] = 'attachment; filename = "PaymentReport.csv"'

    return response


############################################################################################################


# find employee
def employee_find(request):
    empDataKey = request.POST.get('empID')

    searchedEmp = Employee.objects.get(id=empDataKey)

    empName = searchedEmp.empName
    empBasic = searchedEmp.basicWage

    salform = PaymentForm()
    allo = Allowances.objects.all()
    ded = Deductions.objects.all()

    context = {
        'empName': empName,
        'émpBasic': empBasic,
        'form': salform,
        'allowanceFF': allo,
        'empDataKey': empDataKey,
        'ded': ded

    }

    return render(request, 'ePayments/ePayments_form.html', context)


# calculate salary
def calculate(request):
    eID = request.POST.get('eID')
    eName = request.POST.get('eName')
    basic = request.POST.get('basic')
    allo = request.POST.get('allo')
    ded = request.POST.get('ded')
    date = request.POST.get('date')

    netPay = (float(basic) + float(allo) - float(ded))

    context = {
        'éid': eID,
        'éname': eName,
        'basic': basic,
        'allo': allo,
        'ded': ded,
        'netPay': netPay,
        'date': date
    }

    if request.method == 'POST':
        # paySlip = PaySlip.objects.create(empID=eID,empName=eName,basicWage=basic, allowance=allo,deduction=ded,netPay=netPay)

        allow = Allowances.objects.get(amount=allo)

        # deduc = Deductions.objects.get(amount=ded)
        try:
            deduc = Deductions.objects.get(amount=ded)
        except MultipleObjectsReturned:
            deduc = Deductions.objects.filter(amount=ded)

        paySlip = PaySlip(empID=eID, empName=eName, basicWage=basic, month=date, allowance=allow, deduction=deduc,
                          netPay=netPay)

        paySlip.save()

    return render(request, 'ePayments/ePayments_form.html', context)
