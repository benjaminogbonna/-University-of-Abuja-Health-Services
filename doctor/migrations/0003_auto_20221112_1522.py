# Generated by Django 3.0 on 2022-11-12 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0002_remove_doctor_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='gender',
            field=models.CharField(blank=True, choices=[('female', 'Female'), ('male', 'Male')], default='', max_length=30),
        ),
    ]
