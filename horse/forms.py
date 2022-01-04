from django import forms
from django.forms import ModelForm
from .models import Image

class ImageForm(ModelForm):
    class Meta:
        model= Image
        fields = ['comment', 'horse', 'name']
        