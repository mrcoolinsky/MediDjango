# Generated by Django 4.2.7 on 2023-12-06 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_patient_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='phone_number',
            field=models.CharField(default='', max_length=9),
        ),
    ]
