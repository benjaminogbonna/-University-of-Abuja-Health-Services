from django.db import models
from django.contrib.auth.models import User


class Receptionist(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=12, blank=True, default='')
    address = models.CharField(max_length=200, blank=True, default='')

    def __str__(self):
        return f'{self.username}'


class Contact(models.Model):
    name = models.CharField(verbose_name='Name', max_length=50, null=False, blank=False)
    email = models.EmailField(verbose_name='Email', max_length=50, null=False, blank=False)
    subject = models.CharField(verbose_name='Subject', max_length=255, null=False, blank=False)
    message = models.TextField(verbose_name='Message')
    date_sent = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_sent',)

    def __str__(self):
        return f'Email from {self.name}'