from django import forms

class UserLoginForm(forms.Form):
    nazwa = forms.CharField(label="Twój login: ",
                            max_length=40,
                            required=True,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    haslo = forms.CharField(label="Twoje hasło: ",
                            required=True,
                            widget=forms.TextInput(attrs={'type': 'password', 'class': 'form-control'}))