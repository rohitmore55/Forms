from django import forms
from .models import DefaultFormData

class DefaultForm(forms.ModelForm):
    class Meta:
        model = DefaultFormData
        fields = ['name', 'rollno', 'date_of_birth', 'age', 'class_field']
