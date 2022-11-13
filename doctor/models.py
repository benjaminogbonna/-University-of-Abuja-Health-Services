from django.db import models
from django.contrib.auth.models import User


class Doctor(models.Model):
    GENDER = (
        ('female', 'Female'),
        ('male', 'Male'),
    )
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=12, default="", blank=True)
    gender = models.CharField(choices=GENDER, max_length=30, blank=True, default='')
    department = models.CharField(max_length=30, blank=True, default='')
    address = models.CharField(max_length=200, blank=True, default='')

    def __str__(self):
        return f'Dr {self.username.first_name} {self.username.last_name}: {self.department}'
