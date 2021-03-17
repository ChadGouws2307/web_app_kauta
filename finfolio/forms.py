from django import forms
from .models import Trade, TradeFile


class TradeForm(forms.ModelForm):
    class Meta:
        model = Trade
        fields = ['ticker', 'date', 'price', 'no_of_shares']


class TradeFileForm(forms.ModelForm):
    class Meta:
        model = TradeFile
        fields = ['trade_file']
