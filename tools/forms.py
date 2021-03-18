from django import forms
from django.forms.widgets import NumberInput

from .models import PCAFile


class PCAFileForm(forms.ModelForm):
    class Meta:
        model = PCAFile
        fields = ['pca_file', 'no_of_components']
