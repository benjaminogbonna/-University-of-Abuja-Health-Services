from django.db import models
from django.contrib.auth.models import User
from doctor.models import Doctor


class Patient(models.Model):
    GENDER = (
        ('female', 'Female'),
        ('male', 'Male'),
    )
    BLOOD_GROUP = (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    )
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=12, unique=True)
    phone = models.CharField(max_length=20, blank=True, default='')
    gender = models.CharField(choices=GENDER, max_length=30, blank=True, default='')
    age = models.PositiveIntegerField(default=0, blank=True)
    department = models.CharField(max_length=255, blank=True, default='')
    level = models.CharField(max_length=20, blank=True, default='')
    blood_group = models.CharField(choices=BLOOD_GROUP, max_length=20, blank=True, default='')
    genotype = models.CharField(max_length=20, blank=True, default='')
    address = models.CharField(max_length=200, blank=True, default='')

    def __str__(self):
        return f'{self.username}-{self.username.first_name}'


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, related_name='appointments', on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, related_name='appointments', on_delete=models.CASCADE)
    time = models.TimeField(blank=False)
    date = models.DateField(blank=False)
    purpose = models.TextField(blank=False)
    approved = models.BooleanField(max_length=15, default=False)
    completed = models.BooleanField(max_length=15, default=False)

    def __str__(self):
        return f'Appointment for: Dr {self.doctor} and {self.patient}'
