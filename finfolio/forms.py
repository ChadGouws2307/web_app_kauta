from django import forms
from .models import Trade


class TradeForm(forms.ModelForm):

    class Meta:
        model = Trade
        fields = ['company', 'no_of_shares', 'date', 'price']
