from django.shortcuts import render
from student.forms import *
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from HR.models import *
import csv
import random

# Create your views here.

def login_required(func):
    def inner(request,*args, **kwargs):
        un=request.session.get('username')
        if un:
            print(un)
            return func(request, *args,**kwargs)
        return HttpResponseRedirect(reverse('student_login'))
    return inner


def student_home(request):
    # un=request.session.get('username')
    # if un:
    #     UO=User.objects.get(username=un)
    #     PO=StudentProfile.objects.get(username=UO)
    #     d={'UO':UO, 'PO':PO}
    #     return render(request, 'student/student_home.html', d)
    un=request.session.get('username')
    if un:
        UO=User.objects.get(username=un)
        PO=StudentProfile.objects.get(username=UO)
        d={'UO':UO, 'PO':PO}
        return render(request, 'student/student_home.html', d)
    return render(request,'student/student_home.html')

def student_register(request):
    # ESUFO=StudentUserForm()
    # ESPFO=StudentProfileForm()
    # d={'ESUFO':ESUFO, 'ESPFO':ESPFO}
    # if request.method == 'POST' and request.FILES:
    #     SUFDO=StudentUserForm(request.POST)
    #     SPFDO=StudentProfileForm(request.POST, request.FILES)
    #     if SUFDO.is_valid() and SPFDO.is_valid():
    #         pw=SUFDO.cleaned_data.get('password')
    #         MSUFDO=SUFDO.save(commit=False)
    #         MSUFDO.set_password(pw)
    #         MSUFDO.save()
    #         MSPFDO=SPFDO.save(commit=False)
    #         MSPFDO.username=MSUFDO
    #         MSPFDO.save()
    #         return HttpResponseRedirect(reverse('student_login'))
    #     return HttpResponse('Invalid data')
    # return render(request, 'student/student_register.html',d)

    with open(r"C:\Users\User\Downloads\Slot_smaraki1003.csv", "r") as file:
        # Create a CSV reader project 
        csv_reader=csv.reader(file)
        next(csv_reader)
        # Read and print each row
        for i in csv_reader:
            UO=User(first_name=i[1], last_name=i[2], email=i[6], username=i[1]+i[2])
            UO.save()
            PO=StudentProfile(username=UO, pno=i[5])
            PO.save()
    return HttpResponse('Done.....')


def student_login(request):
    if request.method=='POST':
        un=request.POST.get('un')
        pw=request.POST.get('pw')
        AUO=authenticate(username=un, password=pw)
        if AUO:
            login(request,AUO)
            request.session['username']=un
            return HttpResponseRedirect(reverse('student_home'))
        return HttpResponse('Invalid Credentials')
    return render(request, 'student/student_login.html')

@login_required
def student_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('student_home'))

@login_required
def mock_ratings(request):
    all_ratings=Ratings.objects.all()
    d={'all_ratings' : all_ratings}
    return render(request, 'student/mock_ratings.html',d)

@login_required
def student_display_profile(request):
    un=request.session.get('username')
    if un:
        UO=User.objects.get(username=un)
        PO=StudentProfile.objects.get(username=UO)
        d={'UO':UO, 'PO':PO}
        print(UO)
        print(PO)
        return render(request, 'student/student_display_profile.html',d)
    return render(request,'student/student_display_profile.html')

def student_un(request):
    if request.method == 'POST':
        un=request.POST.get('un')
        UO=request.session.get(username=un)
        if UO:
            otp=random.randint(1000,9999)
            print(otp)
            return HttpResponseRedirect(reverse('student_otp'))
    return render(request,'student/student_un.html')


def student_otp(request):
    return render(request, 'student/student_otp.html')