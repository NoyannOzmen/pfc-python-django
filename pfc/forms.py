from django import forms
from .models import Media

class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Media
        fields = ('ordre', 'association', 'animal', 'url')
        widgets = {'ordre' : forms.HiddenInput(), 'association' : forms.HiddenInput(), 'animal' : forms.HiddenInput()}