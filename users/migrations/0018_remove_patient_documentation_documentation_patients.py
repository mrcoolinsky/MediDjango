# Generated by Django 4.2.7 on 2023-11-15 23:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_patient_documentation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='Documentation',
        ),
        migrations.AddField(
            model_name='documentation',
            name='patients',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='users.patient'),
        ),
    ]
