# Generated by Django 3.0 on 2022-11-12 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_remove_patient_medical_report'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='name',
        ),
    ]