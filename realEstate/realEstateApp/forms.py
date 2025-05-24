from django import forms
from .models import *


class RealEstateForm(forms.ModelForm):
    characteristics_display = forms.CharField(
        label='Characteristics',
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'readonly': 'readonly',
            'rows': 3
        })
    )

    class Meta:
        model = RealEstate
        fields = ['name', 'description', 'area', 'date', 'image', 'isBooked', 'isSold']  # без characteristics

    def __init__(self, *args, **kwargs):
        characteristics_str = kwargs.pop('characteristics_str', '')
        super().__init__(*args, **kwargs)
        self.fields['characteristics_display'].initial = characteristics_str

        for field_name, field in self.fields.items():
            if not isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-control'
