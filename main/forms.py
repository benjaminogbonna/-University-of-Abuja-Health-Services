from django import forms
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(forms.Form):
    username = forms.CharField(label='',
                               widget=forms.TextInput(attrs={'placeholder': 'Username or Reg number',
                                                             'class': 'form-control'}))
    password = forms.CharField(label='',
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                 'class': 'form-control'}))
