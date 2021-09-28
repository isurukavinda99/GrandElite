import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
import csv
from .models import *
from .forms import *
from django.contrib import messages
from .filters import FilterEmployee, FilterSalary, FilterAttRecs, FilterInOutStat
from django.contrib.auth.decorators import login_required
from CAS.decorators import *

#xhtml2 views imports


from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

@login_required(login_url='login')
@allowed_users(allowed_roles=['EMS'])
def exportAsCsv(request):

    result = HttpResponse(content_type='text/csv')

    writer = csv.writer(result)
    writer.writerow(['Employee ID','First Name','Last Name','NIC'])

    for user in EmployeeData.objects.all().values_list('id','firstName','lastName','nic'):

        writer.writerow(user)

    result['Content-Disposition'] = 'attachment; filename = "UserList.csv"'

    return result

@login_required(login_url='login')
@allowed_users(allowed_roles=['EMS'])
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

@login_required(login_url='login')
@allowed_users(allowed_roles=['EMS'])
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

@login_required(login_url='login')
@allowed_users(allowed_roles=['EMS'])
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

@login_required(login_url='login')
@allowed_users(allowed_roles=['EMS'])
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



    #filtering Attendance Records and render to template

    currentDate = datetime.date.today();
    totAttendedEmp = Attendance.objects.filter(date=currentDate).count()

    todayEmp = EmployeeData.objects.filter(attendanaceData__date=currentDate);

    atFoa = todayEmp.filter(position=1).count()

    atSk = todayEmp.filter(position=2).count()

    atEc = todayEmp.filter(position=3).count()

    atMaid = todayEmp.filter(position=4).count()

    atWait = todayEmp.filter(position=5).count()











    context = {
        'activeEmpCount':empActiveCount,
        'foa':foa,
        'stk':sk,
        'chef':ec,
        'maid':maid,
        'waiter':waiter,
        'attendandAllemp':totAttendedEmp,
        'AtFoa':atFoa,
        'Atsk':atSk,
        'Atec':atEc,
        'AtMaid':atMaid,
        'AtWait':atMaid

    }




    return render(request,'EMS/emp-dashboard.html',context)

#views for employee salary groups
@login_required(login_url='login')
@allowed_users(allowed_roles=['EMS'])
def salary_grp_list(request):


    allSalaryData = SalaryGroup.objects.all()

    myFilter = FilterSalary(request.GET, queryset=allSalaryData)

    allSalaryData = myFilter.qs

    context = {'salGrp':allSalaryData,
               'sarchSal':myFilter

               }

    return render(request,'EMS/eams-salary-group-list.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['EMS'])
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


# views for employee list
@login_required(login_url='login')
@allowed_users(allowed_roles=['EMS'])
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

    searchKey = (request.GET.get('empSearch'))



    searchedEmployee = valid_employees.filter(id=searchKey).first()

    #print(searchedEmployee.firstName)






    if request.method == 'POST':



        empId = request.POST.get('empId')

        print(empId)

        empName = request.POST.get('empName')
        print(empName)

        inTime = request.POST.get('empInTime')
        print(inTime)

        date = request.POST.get('tDate')
        print(date)

        convertedTime = int(inTime.replace(':', ''))
        print(convertedTime)

        if convertedTime > 800:
            status = 'late'
            print(status)

        else:
            status = 'On Time'


        IntimeData = Attendance(emp_at_id=empId, emp_at_name=empName, date=date, inTime=inTime, inStatus=status)

        IntimeData.save()
        messages.success(request,'In time Marked')

        # empinTimeData = EmployeeData(attendanaceData=IntimeData)
        # empinTimeData.

        #searchedEmployee.attendanaceData = IntimeData
        searchedEmployee.attendanaceData.add(IntimeData)
        searchedEmployee.save()


        return HttpResponseRedirect(reverse('inPortal'))
















    context = {
        'validList':valid_employees,
        'results':searchedEmployee

    }




    return render(request, 'AMS/In_portal.html', context)


def AttendanceList(request):


    #attendanceData = Attendance.objects.all()

    empAll = EmployeeData.objects.filter(empStatus=1)

    attFilter = FilterAttRecs(request.GET,queryset=empAll)
    empAll = attFilter.qs

    # attAll = Attendance.objects.all()
    #
    # statFilt = FilterInOutStat(request.GET,queryset=attAll)
    # attAll = statFilt.qs





    context = {
        #'attendanceRecord':attendanceData,
        'allEmpData':empAll,
        'filtering':attFilter,
        # 'stat':statFilt
    }



    return render(request,'AMS/Attendance_List.html',context)

def MarkOutTime(request):


    searchId = request.GET.get('empOutSearch')

    #onlyOnTime = .filter(inStatus='Late' or 'On Time')

    onlyPending = Attendance.objects.filter(overallStatus='pending')

    empData = onlyPending.filter(emp_at_id=searchId).first()





    empImageRes = EmployeeData.objects.filter(id=searchId).first()

    if request.method == 'POST':

        empId = request.POST.get('empId')

        print(empId)

        empName = request.POST.get('empName')
        print(empName)

        inTime = request.POST.get('empInTime')
        print(inTime)

        date = request.POST.get('tDate')
        print(date)

        empOutTime = request.POST.get('empOutTime')

        convertedOutTime = int(empOutTime.replace(':', ''))

        if convertedOutTime < 1700:
            oStatus = 'Early'

        elif 1700 < convertedOutTime < 1730:
            oStatus = 'Leaved'

        else:
            oStatus = 'Still Working'


        print(convertedOutTime)
        print(oStatus)




        empData.overallStatus = 'completed'
        empData.outTime = empOutTime
        empData.outStatus = oStatus


        #outtimeData = Attendance(emp_at_id=empId, emp_at_name=empName, date=date, inTime=inTime, inStatus='on Time',outTime=empOutTime, outStatus=oStatus,overallStatus='Completed')
        #outtimeData.save()

        empData.save()

        #empImageRes.attendanaceData.outTime = empOutTime


        #empImageRes.attendanaceData.outStatus = oStatus


        #empImageRes.attendanaceData.overallStatus = 'completed'


        #empImageRes.attendanaceData.save()


        messages.success(request,'Out time Marked Successfully')

        return HttpResponseRedirect(reverse('viewRec'))



    context = {
        'attData':empData,
        'image':empImageRes
    }



    return render(request,'AMS/Out Portal.html',context)



# def displayAttRec(request,pk):
#     attendanceData = Attendance.objects.filter(emp_at_id=pk).first()
#
#     print(attendanceData.date)
#     print(attendanceData.inTime)
#
#
#     context = {
#         'relatedData':attendanceData
#     }
#
#     return render(request,'AMS/Attendance_List.html',context)

def SearchEmpByStatus(request):

    searchDate = request.POST.get('searchDate')

    print()

    #searchAllByDate = Attendance.objects.filter(date=searchDate)
    emp=[]

    for e in EmployeeData.objects.all():
        emp.append({"e":e,"a":Attendance.objects.filter(date=searchDate,emp_at_id=e.id).all()})



    #searchDateRec = Attendance.objects.filter(date=searchDate)

    #print({searchDateRec})
    #print(searchDateRec.first().emp_at_name)



    # print({searchAll})











    context = {
        'dateEmp':emp,


    }


    return render(request,'AMS/Attendance_List_date.html',context)





def attendancelist_render_pdf_view(request):

    my = request.POST.get('reportDat')

    totDate = datetime.datetime.strptime(my,"%Y-%m")

    year = totDate.year

    month = totDate.month




    #attendanceRep = EmployeeData.objects.filter(attendanaceData__date__month=atMonth, attendanaceData__date__year=atYear)

    rec = []
    for e in EmployeeData.objects.all():
        rec.append({"e":e,"a":Attendance.objects.filter(date__month=month, date__year=year,emp_at_id=e.id).all()})

    template_path = 'AMS/attendance_repot_pdf.html'
    context = {'attData': rec,'Year':year,'Month':month}
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