from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def LoginPage(requst):
    if requst.method == 'POST':

        un = requst.POST.get('username')
        pwd = requst.POST.get('password')

        user = authenticate(requst, username=un, password=pwd)


        if user is not None:
            login(requst,user)
            group = requst.user.groups.filter(user=requst.user)[0]


            if group.name == 'EMS':
                return redirect('eams-dashboard')

            elif group.name == 'PMS':
                return redirect('/pms')
            elif group.name == 'ISMS':
                return  redirect('/isms')
            elif group.name == 'RAE':
                return redirect('/rae/room_list/')



        else:
            messages.error(requst,'username or password is incorrect')



    return render(requst, 'Login/login.html')

def LogoutUser(request):
    logout(request)
    return redirect('login')