from django import forms
from patient.models import Appointment
from .models import Doctor


class ProfileEditForm(forms.ModelForm):
    """Doctor edit form"""

    class Meta:
        model = Doctor
        fields = ('phone', 'gender', 'department', 'address')

        # labels = {
        #     'phone': '',
        # }

        widgets = {
            'phone': forms.TextInput(attrs={'placeholder': 'Phone', 'class': 'form-control'}),
            'gender': forms.Select(attrs={'placeholder': 'Gender', 'class': 'form-control'}),
            'department': forms.TextInput(attrs={'placeholder': 'Department', 'class': 'form-control'}),
            'address': forms.TextInput(attrs={'placeholder': 'Enter your address', 'class': 'form-control'}),
        }


class AppointmentEditForm(forms.ModelForm):
    """Appointment edit form"""

    class Meta:
        model = Appointment
        fields = ('time', 'date', 'purpose', 'approved', 'completed')

        # labels = {
        #     'phone': '',
        # }

        widgets = {
            'time': forms.TimeInput(attrs={'type': 'time', 'placeholder': 'Choose time', 'class': 'form-control'}),
            'date': forms.DateInput(attrs={'type': 'date', 'placeholder': 'Choose date', 'class': 'form-control'}),
            'purpose': forms.Textarea(attrs={'readonly': 'readonly', 'placeholder': 'Purpose of appointment.',
                                             'class': 'form-control'}),
        }
