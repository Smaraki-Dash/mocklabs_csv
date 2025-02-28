from django import forms
from student.models import *

class StudentUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email','username','password']
        help_texts={'username': ''}

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model=StudentProfile
        exclude=['username']
        help_texts={'profile_pic': "please enter a 'formal photo' " ,
                    'resume': 'keep update your resume before every MOCK'}
