from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from manager.models import *
from Trainer.forms import *
from  HR.models import *
# from django.contrib.auth.decorators import login_required

# Create your views here.
def Trainer_login_required(func):
    def inner(request, *args, **kwargs):
        tu=request.session.get('traineruser')
        if tu:
            # print(tu)
            return func(request, *args, **kwargs)
        return HttpResponseRedirect(reverse('Trainer_login'))
    return inner



def Trainer_home(request):
    return render(request, 'Trainer/Trainer_home.html')

def Trainer_login(request):
    if request.method=='POST':
        un=request.POST.get('un')
        pw=request.POST.get('pw')
        AUO=authenticate(username=un, password=pw)
        if AUO.is_active and AUO.is_staff:
            trainer_emp = EmployeeProfile.objects.get(username=AUO)
            if trainer_emp.role == 'Trainer':
                login(request, AUO)
                request.session['traineruser']=un
                return HttpResponseRedirect(reverse('Trainer_home'))
            return HttpResponse("can't login, you are not a trainer")
        return HttpResponse('Invalid user credentials')
    return render(request, 'Trainer/Trainer_login.html')

@Trainer_login_required
def Trainer_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('Trainer_home'))

@Trainer_login_required
def start_mock(request):
    ERFO=RatingForm()
    all_objects=User.objects.all()
    d={'ERFO': ERFO, 'SO':all_objects}
    if request.method == 'POST':
        RFDO = RatingForm(request.POST)
        search=request.POST.get('search')
        if search:
            SO=User.objects.get(username=search) 
            print(SO) 
            d['SO'] = SO            
            if RFDO.is_valid():       
                trainer=request.session.get('traineruser')
                TO=User.objects.get(username=trainer) 
                MRFDO=RFDO.save(commit=False) 
                MRFDO.conducted_by = TO 
                MRFDO.student = SO  
                MRFDO.save() 
                return HttpResponseRedirect(reverse('start_mock')) 
            return HttpResponse('Trainer user not found')
        return HttpResponse('User not found')
    return render(request, 'Trainer/start_mock.html',d) 

