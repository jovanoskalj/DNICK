from django import forms
from .models import *

class TravelForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(TravelForm,self).__init__(*args,**kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


    class Meta:
            model = Travel
            exclude = ['guide']


