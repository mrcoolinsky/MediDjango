# Generated by Django 4.2.7 on 2023-12-10 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_doctor_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicine',
            name='availability',
        ),
    ]
