from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
import csv
from .models import *
from .forms import *
from django.contrib import messages
from .filters import FilterEmployee, FilterSalary


#xhtml2 views imports


from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


def exportAsCsv(request):

    result = HttpResponse(content_type='text/csv')

    writer = csv.writer(result)
    writer.writerow(['Employee ID','First Name','Last Name','NIC'])

    for user in EmployeeData.objects.all().values_list('id','firstName','lastName','nic'):

        writer.writerow(user)

    result['Content-Disposition'] = 'attachment; filename = "UserList.csv"'

    return result


def render_pdf_view(request):
    template_path = 'EMS/user-profile-pdf.html'
    context = {'myvar': 'this is your template context'}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')

    #if user dont need to view pdf then use below response
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    #if user need to view and download pdf
    response['Content-Disposition'] = 'filename="report.pdf"'

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


def user_render_pdf_view(request,pk):

    userData = EmployeeData.objects.get(id=pk)

    template_path = 'EMS/user-profile-pdf.html'
    context = {'empData': userData}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')

    #if user dont need to view pdf then use below response
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    #if user need to view and download pdf
    response['Content-Disposition'] = 'filename="report.pdf"'

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

def userList_render_pdf_view(request):

    userList= EmployeeData.objects.all()

    template_path = 'EMS/user-List-pdf.html'
    context = {'empList': userList}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')

    #if user dont need to view pdf then use below response
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    #if user need to view and download pdf
    response['Content-Disposition'] = 'filename="report.pdf"'

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





# Create your views here.

#views for emp dashboard
def dashboard(request):
    empActiveCountTot = EmployeeData.objects.filter(empStatus=True)

    empActiveCount = EmployeeData.objects.filter(empStatus=True).count()

    allEmp = EmployeeData.objects.all()


    #front office attendant
    foa = empActiveCountTot.filter(position=1).count()

    #store keeper
    sk = empActiveCountTot.filter(position=2).count()

    #executive chef
    ec = empActiveCountTot.filter(position=3).count()

    #maid
    maid = empActiveCountTot.filter(position=4).count()

    #waiter
    waiter = empActiveCountTot.filter(position=5).count()

    context = {
        'activeEmpCount':empActiveCount,
        'foa':foa,
        'stk':sk,
        'chef':ec,
        'maid':maid,
        'waiter':waiter

    }




    return render(request,'EMS/emp-dashboard.html',context)

#views for employee salary groups
def salary_grp_list(request):


    allSalaryData = SalaryGroup.objects.all()

    myFilter = FilterSalary(request.GET, queryset=allSalaryData)

    allSalaryData = myFilter.qs

    context = {'salGrp':allSalaryData,
               'sarchSal':myFilter

               }

    return render(request,'EMS/eams-salary-group-list.html',context)


def addSalaryGroup(request):

    addSalForm = SalaryAddForm()

    if request.method == 'POST':

        addSalForm = SalaryAddForm(request.POST)

        if addSalForm.is_valid():
            addSalForm.save()

            messages.success(request,"Salary Group Added Successfully!")
            return redirect('/emp/salary/')

    context = {
        'addSal':addSalForm
    }

    return render(request,'EMS/salary-inup.html',context)


#views for employee list
def employee_list(request):

    allEmployeeData = EmployeeData.objects.all()


    # jobId = int(request.POST.get('jobSelect'))
    #
    # empAllData = EmployeeData.objects.all()
    #
    #
    #
    # searchByJob = empAllData.filter(position=jobId)
    #

    # #front office attendant
    # foa = empAllData.filter(position='1')
    #
    # #store keeper
    # sk = empAllData.filter(position=2)
    #
    # #executive chef
    # ec = empAllData.filter(position=3)
    #
    # #maid
    # maid = empAllData.filter(position=4)
    #
    # #waiter
    # waiter = empAllData.filter(position=5)




    myFilter = FilterEmployee(request.GET, queryset=allEmployeeData)

    allEmployeeData = myFilter.qs










    context = {'empData':allEmployeeData,
               'statusFilter':myFilter,


               }


    return render(request,'EMS/eams-emp-list.html',context)

#views for employee profile
def employee_profile(request,pk):

    employee_details = EmployeeData.objects.get(id=pk)

    context = {
        'userData': employee_details
    }

    return render(request,'EMS/eams-user-profile.html',context)

def insertEmployee(request):

    addEmpForm = EmployeeAddForm()

    if request.method == 'POST':
        addEmpForm = EmployeeAddForm(request.POST,request.FILES)

        if addEmpForm.is_valid():
            addEmpForm.save()

            messages.success(request, "Employee Added Successfully!")


            return redirect('/emp/employees/')

    context = { 'addEmp':addEmpForm}

    return render(request, 'EMS/eams-add-user.html',context)

def updateEmployee(request,pk):

    empExData = EmployeeData.objects.get(id=pk)

    updateEmpForm = EmployeeAddForm(instance=empExData)
    context = {
        'addEmp': updateEmpForm,
        'empRecord':empExData
    }


    if request.method == 'POST':
        addEmpForm = EmployeeAddForm(request.POST, request.FILES, instance=empExData)

        if addEmpForm.is_valid():
            addEmpForm.save()

            messages.success(request, "Employee Updated Successfully!")

            return redirect('/emp/employees/')

    return render(request, 'EMS/eams-update-user.html', context)


def switchEmployee(request,pk):


    pwd = request.POST.get('deletePwd')

    realPWD = "abcdef"

    employeeStatus = EmployeeData.objects.get(id = pk)

    if(pwd == realPWD):


        if employeeStatus.empStatus == 1:

            employeeStatus.empStatus = 0

            employeeStatus.save()

            messages.success(request, "Employee Deleted Successfully!")

    else:

        messages.error(request, "Authorization Failed!")



    return HttpResponseRedirect(reverse("eams-empList"))

def reallocateEmp(request,pk):


    pwd = request.POST.get('allowPwd')

    realPWD = "abcdef"


    employeeStatus = EmployeeData.objects.get(id = pk)



    if (pwd == realPWD):

        if employeeStatus.empStatus == 0:

            employeeStatus.empStatus = 1

            employeeStatus.save()

            messages.success(request, "Employee Rehired Successfully!")


    else:

        messages.error(request, "Authorization Failed!")






    return HttpResponseRedirect(reverse("eams-empList"))




def updateSal(request,pk):

    salExData = SalaryGroup.objects.get(id=pk)

    updateSalForm = SalaryAddForm(instance=salExData)
    context = {
        'updtSal': updateSalForm,
        'salRecord':salExData
    }


    if request.method == 'POST':
        updateSalForm = SalaryAddForm(request.POST, request.FILES, instance=salExData)

        if updateSalForm.is_valid():
            updateSalForm.save()

            messages.success(request, "Salary Group Updated Successfully!")

            return redirect('/emp/salary/')

    return render(request, 'EMS/salary-updt.html', context)



def deleteSal(request,pk):

    salaryData = SalaryGroup.objects.get(id=pk)

    if request.method == "POST":
        salaryData.delete()
        return redirect('/emp/salary/')

    context = { 'deleteSalary',salaryData}

    return render(request,'EMS/eams-salary-group-list.html')




################Attendance Management System URL ###################################

def inPortal(request):

    valid_employees = EmployeeData.objects.filter(empStatus=1)

    searchKey = request.GET.get('empSearch')

    searchRec = valid_employees.get(id=searchKey)

    empId = request.GET.get('empId')
    empName = request.GET.get('name')
    inTime = request.GET.get('inTime')


    date = request.GET.get('currentDate')

 #   if 83000 > inTimeComp > 80000:
  #      empInStat = 'Late'

   # elif  inTimeComp > 83000:
    #    empInStat = 'Absent'

    #else:
     #   empInStat = 'On Time'


    #IntimeData = Attendance(emp_at_id=empId,emp_at_name=empName,date=date,inTime=inTime,inStatus=empInStat)
    #IntimeData.save()

    #print(searchKey)
    print(inTime)
    print(empName)



    context = {
        'validList':valid_employees,
        'searchDet':searchRec
    }




    return render(request, 'AMS/In_portal.html', context)


