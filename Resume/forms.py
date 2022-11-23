from .models import *
from django import forms

class CVform(forms.ModelForm):

    class Meta:
        model = CV
        fields = '__all__'