from django import forms
from .models import *

class  ReservationForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(ReservationForm,self).__init__(*args,**kwargs)
        for field_name, field in self.fields.items():
            if not isinstance(field.widget,forms.CheckboxInput):
                field.widget.attrs['class']='form-control'


    class Meta:
        model=Reservation
        fields="__all__"
        exclude = ('guest',)
        widgets={
            'start_date': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
            'end_date': forms.DateInput(attrs={'class':'form-control', 'type':'date'})

        }
