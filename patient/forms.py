from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Patient, Appointment


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
            'age': forms.NumberInput(attrs={'placeholder': 'Age', 'class': 'form-control'}),
            'department': forms.TextInput(attrs={'placeholder': 'Department', 'class': 'form-control'}),
            'level': forms.NumberInput(attrs={'placeholder': 'Level', 'class': 'form-control'}),
            'blood_group': forms.Select(attrs={'placeholder': 'Gender', 'class': 'form-control'}),
            'genotype': forms.TextInput(attrs={'placeholder': 'Genotype', 'class': 'form-control'}),
            'address': forms.TextInput(attrs={'placeholder': 'Enter your address', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(ProfileEditForm, self).__init__(*args, **kwargs)
        self.fields['age'].widget.attrs['min'] = 0
        self.fields['level'].widget.attrs['min'] = 0


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('doctor', 'time', 'date', 'purpose')
        labels = {
            'doctor': 'Select Doctor',
            'time': 'Choose time',
            'date': 'Choose date',
        }

        widgets = {
            'doctor': forms.Select(attrs={'placeholder': 'Select Doctor', 'class': 'form-control'}),
            'time': forms.TimeInput(attrs={'type': 'time', 'placeholder': 'Choose time', 'class': 'form-control'}),
            'date': forms.DateInput(attrs={'type': 'date', 'placeholder': 'Choose date', 'class': 'form-control'}),
            'purpose': forms.Textarea(attrs={'placeholder': 'Purpose of appointment. Please be descriptive enough',
                                             'class': 'form-control'}),
        }

