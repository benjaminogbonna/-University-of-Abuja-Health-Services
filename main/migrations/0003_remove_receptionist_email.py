# Generated by Django 3.0 on 2022-11-12 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20221112_0830'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receptionist',
            name='email',
        ),
    ]
