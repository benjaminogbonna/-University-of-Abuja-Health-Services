from django.db import models
from django.contrib.auth.models import User


class Receptionist(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=12, blank=True, default='')
    address = models.CharField(max_length=200, blank=True, default='')

    def __str__(self):
        return f'{self.username}'
