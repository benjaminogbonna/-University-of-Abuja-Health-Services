# Generated by Django 3.0 on 2022-11-12 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='status',
            new_name='completed',
        ),
    ]
