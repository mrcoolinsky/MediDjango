# Generated by Django 4.2.7 on 2024-01-09 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_alter_visit_medicine_dosage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='date',
            field=models.DateField(),
        ),
    ]
