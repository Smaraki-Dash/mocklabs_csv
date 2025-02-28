from django import forms
from manager.models import *

class EmplyeeUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name', 'last_name', 'email']

roles=[
        ('HR', 'HR'),
        ('Trainer', 'Trainer')
    ]

class EmployeeProfileForm(forms.ModelForm):
    class Meta:
        model=EmployeeProfile
        exclude=['username']
        widgets={'role': forms.RadioSelect(choices=roles)}