from django import forms
from django .forms import ModelForm
from . models import india

class indiaform(forms.ModelForm):
    class Meta:
        model=india
        fields="__all__"