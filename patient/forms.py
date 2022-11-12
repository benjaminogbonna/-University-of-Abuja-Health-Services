from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import Patient


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='',
                               widget=forms.TextInput(attrs={'placeholder': 'Reg number',
                                                             'class': 'form-control'}))
    password = forms.CharField(label='',
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                 'class': 'form-control'}))


class ProfileEditForm(forms.ModelForm):
    """Patient edit form"""

    class Meta:
        model = Patient
        fields = ('phone', 'gender', 'age', 'department', 'level', 'blood_group', 'genotype', 'address')

        labels = {
            'phone': '',
        }

        widgets = {
            'phone': forms.TextInput(attrs={'placeholder': 'Phone', 'class': 'form-control'}),
            'gender': forms.Select(attrs={'placeholder': 'Gender', 'class': 'form-control'}),
            'age': forms.TextInput(attrs={'placeholder': 'Age', 'class': 'form-control'}),
            'department': forms.TextInput(attrs={'placeholder': 'Department', 'class': 'form-control'}),
            'level': forms.TextInput(attrs={'placeholder': 'Level', 'class': 'form-control'}),
            'blood_group': forms.Select(attrs={'placeholder': 'Gender', 'class': 'form-control'}),
            'genotype': forms.TextInput(attrs={'placeholder': 'Genotype', 'class': 'form-control'}),
            'address': forms.TextInput(attrs={'placeholder': 'Enter your address', 'class': 'form-control'}),
        }
