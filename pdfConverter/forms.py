import django
from django import forms

from .models import Converter

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Converter
        fields = '__all__'