from django import forms
from .models import Contact


class LoginForm(forms.Form):
    username = forms.CharField(label='',
                               widget=forms.TextInput(attrs={'placeholder': 'Username or Reg number',
                                                             'class': 'form-control'}))
    password = forms.CharField(label='',
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                 'class': 'form-control'}))


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'message')

        labels = {
            'name': '',
            'email': '',
            'subject': '',
            'message': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your name', 'class': 'form-control'}),
            'email': forms.TextInput(attrs={'placeholder': 'Your email', 'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Message subject', 'class': 'form-control'}),
            'message': forms.Textarea(attrs={'placeholder': 'Type message here', 'class': 'form-control'}),
        }
