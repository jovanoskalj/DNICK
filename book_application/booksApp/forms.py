from django import forms

from .models import *




class BookForm(forms.ModelForm):
    def __init__(self, *args ,**kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if not isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = Book
        fields = "__all__"
