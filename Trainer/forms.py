from django import forms
from HR.models import *

class RatingForm(forms.ModelForm):
    class Meta:
        model=Ratings
        exclude=['student', 'conducted_by']

