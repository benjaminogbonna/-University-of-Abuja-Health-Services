# Generated by Django 3.0 on 2022-11-13 00:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0003_auto_20221112_1522'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='status',
        ),
    ]
