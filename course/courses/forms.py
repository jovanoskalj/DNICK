from django import forms
from .models import *


class CourseForm(forms.ModelForm):
    lecturers = forms.CharField(
        label='Lecturers (comma-separated)',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False
    )
    def __init__(self, *args ,**kwargs):

        super(CourseForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if not isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = Course
        exclude=['creator',]
        widgets = {
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }