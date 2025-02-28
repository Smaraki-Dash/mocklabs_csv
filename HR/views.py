from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from manager.models import *
from manager.forms import *
from HR.forms import *
import random
import csv
from django.core.mail import send_mail
 
# Create your views here.
def hr_home(request):
    return render(request, 'hr/hr_home.html')

def hr_login(request):
    if request.method=='POST':
        un=request.POST.get('un')
        pw=request.POST.get('pw')
        AUO=authenticate(username=un, password=pw)
        if AUO.is_active and AUO.is_staff:
            emp_profile=EmployeeProfile.objects.get(username=AUO)
            print(emp_profile.role)
            if emp_profile.role == 'HR':
                login(request, AUO)
                request.session['hruser'] = un
                role=emp_profile.role
                request.session['role']=role
                return HttpResponseRedirect(reverse('hr_home'))
            return HttpResponse("can't login you are not a HR")
        return HttpResponse('Invalid User')
    return render(request, 'hr/hr_login.html')

@login_required
def hr_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('hr_home'))

def hr_un(request):
    if request.method == 'POST':
        un = request.POST.get('un')
        UO = User.objects.get(username=un)
        if UO and UO.is_active and UO.is_staff:
            otp = random.randint(1000, 9999)
            request.session['otp'] = otp
            request.session['hruser'] = un
            print(otp)
            return HttpResponseRedirect(reverse('hr_otp'))
        return HttpResponse('Invalid Username')
    return render(request, 'hr/hr_un.html')

def hr_otp(request):
    if request.method == 'POST':
        uotp = request.POST.get('otp')
        gotp = request.session.get('otp')
        if int(uotp) == gotp:
            return HttpResponseRedirect(reverse('hr_change_pw'))
        return HttpResponse('Invalid OTP')
    return render(request, 'hr/hr_otp.html')

def hr_change_pw(request):
    if request.method == 'POST':
        pw = request.POST.get('pw')
        cpw = request.POST.get('cpw')
        if pw == cpw:
            un = request.session.get('hruser')
            UO = User.objects.get(username=un)
            UO.set_password(pw)
            UO.save()
            return HttpResponseRedirect(reverse('hr_login'))
    return render(request, 'hr/hr_change_pw.html')

# @login_required
# def mock_scheduling(request):
#     ESFO=schedulingform()
#     d={'ESFO': ESFO}
#     if request.method == 'POST' and request.FILES:
#         SFDO=schedulingform(request.POST, request.FILES)
#         if SFDO.is_valid():
#             SFDO.save()
#             with open(f"media/Slots/Slot_{SFDO.cleaned_data.get("trainer").username}.csv", 'r' ) as file:
#                 csv_reader=csv.reader(file)
#                 header=next(csv_reader)
#                 lines=[line for line in csv_reader if len(line) != 0]
#                 first_name=[data[1] for data in lines]
#                 last_name=[data[2] for data in lines]
#                 email=[data[-1] for data in lines]
#                 Date = f"{SFDO.cleaned_data.get('date')}"
#                 Time = f"{SFDO.cleaned_data.get('time')}" 
#                 msg=email_content=f""" Subject: Invitation for Mock Interview – QSpiders Bhubaneswar
#                     Dear,

#                     I hope you’re doing well! We are excited to invite you for a mock interview as part of your preparation at [QSpiders Bhubaneswar]. This session is designed to help you practice and receive constructive feedback before your official interview.

#                     Interview Details:
#                     📅 Date: {Date}
#                     ⏰ Time: {Time}
#                     📍 Location/Platform: QSpiders Bhubaneswar
#                     ⏳ Duration: 30min

#                     During the mock interview, we will focus on [ key topics such as behavioral questions, technical skills, case study, etc.], followed by a feedback session.

#                     Please confirm your availability at your earliest convenience. Feel free to reach out if you have any questions. We look forward to helping you prepare!

#                     Best regards,
#                     [{request.session.get('hruser')}]
#                     [{request.session.get('role')}]
#                     [ QSpiders Bhubaneswar]"""
#                 send_mail(
#                     "Mock Scheduled Successfully",
#                      msg,
#                     'smarakidash1003@gmail.com',
#                     email,
#                     fail_silently=False
#                 )
#             return HttpResponseRedirect(reverse('hr_home'))
#         return HttpResponse('Invalid User')
#     return render(request, 'hr/mock_scheduling.html',d)


def mock_scheduling(request):
    hrun=request.session.get('hruser')
    ESFO=schedulingform()
    d={'ESFO': ESFO}
    UO=User.objects.get(username=hrun)
    PO=EmployeeProfile.objects.get(username=UO)
    print(hrun)
    if request.method == 'POST' and request.FILES:
        SFDO=schedulingform(request.POST, request.FILES)
        if SFDO.is_valid():
            SFDO.save()
            with open(r"C:\Users\User\Downloads\Slot_smaraki1003.csv" , 'r') as file:
                csv_reader=csv.reader(file)
                next(csv_reader)
                usernames=[i[1]+i[2] for i in csv_reader]
                print(usernames)
                for un in usernames:
                    print(un)
                    SO=User.objects.get(username=un)
                    print(SO)
                    email=SO.email
                    message=f'''Dear,

                        I hope you’re doing well! We are excited to invite you for a mock interview as part of your preparation at QSpiders Bhubaneswar. This session is designed to help you practice and receive constructive feedback before your official interview.

                        Interview Details:
                        📅 Date: {SFDO.cleaned_data.get('date')}
                        ⏰ Time: {SFDO.cleaned_data.get('time')}
                        📍 Location/Platform: QSpiders Bhubaneswar
                        ⏳ Duration: 30min

                        During the mock interview, we will focus on [mention key topics such as behavioral questions, technical skills, case study, etc.], followed by a feedback session.

                        Please confirm your availability at your earliest convenience. Feel free to reach out if you have any questions. We look forward to helping you prepare!

                        Best regards,
                        {SO.first_name}
                        {PO.role}
                        QSpiders Bhubaneswar'''
                    send_mail(
                        'Re: Invitation for Mock Interview – QSpiders Bhubaneswar', 
                         message,
                        'smarakidash1003@gmail.com',
                        [email],
                        fail_silently=False
                    )
            return HttpResponseRedirect(reverse('hr_home'))
        return HttpResponse('Invalid User')
    return render(request, 'hr/mock_scheduling.html',d) 
