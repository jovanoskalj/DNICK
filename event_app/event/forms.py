from django import forms
from django.forms import DateTimeInput

from event.models import *

class EventForm(forms.ModelForm):

    def __init__(self, *args ,**kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if not isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-control'
    class Meta:
        exclude = ('user',)
        model = Event
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})}



