from django import forms 
from HR.models import scheduling

class schedulingform(forms.ModelForm):
    class Meta:
        model=scheduling
        exclude=['slot_id']


