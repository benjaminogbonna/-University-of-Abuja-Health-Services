# Generated by Django 4.1.4 on 2022-12-28 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0006_contact"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="receptionist",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]