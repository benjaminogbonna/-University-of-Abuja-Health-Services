from django.db import models
from django.contrib.auth.models import User


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
    name = models.CharField(max_length=100, blank=True, default='')
    card_number = models.CharField(max_length=12, unique=True)
    email = models.CharField(max_length=50, blank=True, default='')
    phone = models.CharField(max_length=20, blank=True, default='')
    gender = models.CharField(choices=GENDER, max_length=30, blank=True, default='')
    age = models.PositiveIntegerField(default=0, blank=True)
    department = models.CharField(max_length=255, blank=True, default='')
    level = models.CharField(max_length=20, blank=True, default='')
    blood_group = models.CharField(choices=BLOOD_GROUP, max_length=20, blank=True, default='')
    genotype = models.CharField(max_length=20, blank=True, default='')
    address = models.CharField(max_length=200, blank=True, default='')

    def __str__(self):
        return f'{self.username}-{self.name}'
