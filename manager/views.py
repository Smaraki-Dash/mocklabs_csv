from django.shortcuts import render
from manager.forms import *
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import random
import string
# Create your views here.
def manager_home(request):
    return render(request, 'manager/manager_home.html')

def add_emplyee(request):
    EEUFO=EmplyeeUserForm()
    EEPFO=EmployeeProfileForm()
    d={'EEUFO':EEUFO, 'EEPFO':EEPFO}
    if request.method=='POST':
        EUFDO=EmplyeeUserForm(request.POST)
        EPFDO=EmployeeProfileForm(request.POST)
        if EUFDO.is_valid() and EPFDO.is_valid():
            pw=''.join([random.choice(string.ascii_letters) for i in range(1,6)])
            un=f"{EUFDO.cleaned_data.get('first_name')}{EPFDO.cleaned_data.get('pno')[-4:]}"
            MEUFDO=EUFDO.save(commit=False)
            MEUFDO.username=un
            MEUFDO.set_password(pw)
            MEUFDO.is_staff=True
            MEUFDO.save()
            MEPFDO=EPFDO.save(commit= False)
            MEPFDO.username=MEUFDO
            MEPFDO.save()
            print(f'username is {un}')
            print(f"password is {pw}")
            email=MEUFDO.email
            msg=f"Hello Employee \n your username is : {un} \n password is : {pw} \n please save it for further informations \n Thank you for registering in our company"
            send_mail(
                'Emplyee added credentials',
                msg,
                'smarakidash1003@gmail.com',
                [email],
                fail_silently=False
            )
            print('st1')
            return HttpResponseRedirect(reverse('manager_home'))
        print('st2')
        return HttpResponse('Invalid credentials')
    print('st3')
    return render(request, 'manager/add_emplyee.html',d)

def manager_login(request):
    if request.method=='POST':
        un=request.POST.get('un')
        pw=request.POST.get('pw')
        AUO=authenticate(username=un, password=pw)
        if AUO and AUO.is_staff and AUO.is_active:
            if AUO.is_superuser:
                login(request,AUO)
                request.session['username']=un
                return HttpResponseRedirect(reverse('manager_home'))
            return HttpResponse('She/He is not a manager')
        return HttpResponse('Invalid User')
    return render(request, 'manager/manager_login.html')

@login_required
def manager_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('manager_home'))
