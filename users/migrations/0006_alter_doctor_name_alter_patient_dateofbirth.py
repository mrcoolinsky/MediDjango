# Generated by Django 4.2.7 on 2023-11-15 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_disease_medicine_patient_visit_documentation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='Name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='patient',
            name='DateOfBirth',
            field=models.DateField(default='', max_length=10),
        ),
    ]
