from django import forms
from .models import uploader

class Imageform(forms.ModelForm):
    class Meta:
        model = uploader
        fields = ("caption","Images")
