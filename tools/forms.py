from django import forms
from django.forms.widgets import NumberInput

from .models import CorrFile


class CorrFileForm(forms.ModelForm):
    corr_file = forms.FileField(max_length=150)

    class Meta:
        model = CorrFile
        fields = ['corr_file']


class PCAFileForm(forms.ModelForm):
    corr_file = forms.FileField(max_length=150)
    no_of_components = forms.IntegerField(max_value=20,
                                          min_value=0,
                                          widget=NumberInput(attrs={'style': 'width:180px',
                                                                    'placeholder': 'No. of Components'}))

    # class Meta:
    #     model = CorrFile
    #     fields = ['corr_file']