from wiadomosci.models import Wiadomosc
from django import forms


class WiadomoscForm(forms.ModelForm):
    class Meta:
        model = Wiadomosc
        fields = ('tresc', 'data_d')
        widgets = {
            'tresc': forms.Textarea(attrs={'cols': 100, 'rows': 3, 'class': 'form-ontrol'}),
            'data_d': forms.DateTimeInput(attrs={'class': 'form-control'}),
        }