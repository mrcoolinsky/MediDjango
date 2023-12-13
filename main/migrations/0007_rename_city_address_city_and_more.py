# Generated by Django 4.2.7 on 2023-12-04 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_patient_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='City',
            new_name='City',
        ),
        migrations.RenameField(
            model_name='address',
            old_name='Number',
            new_name='Number',
        ),
        migrations.RenameField(
            model_name='address',
            old_name='Street',
            new_name='Street',
        ),
        migrations.RenameField(
            model_name='address',
            old_name='Zip_code',
            new_name='Zip_code',
        ),
        migrations.RenameField(
            model_name='doctor',
            old_name='Name',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='doctor',
            old_name='Specialization',
            new_name='Specialization',
        ),
        migrations.RenameField(
            model_name='doctor',
            old_name='Surname',
            new_name='Surname',
        ),

        migrations.AddField(
            model_name='patient',
            name='address',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.address'),
        ),
        migrations.AddField(
            model_name='patient',
            name='date_of_birth',
            field=models.DateField(default='2000-01-01'),
        ),
        migrations.AddField(
            model_name='patient',
            name='name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='patient',
            name='surname',
            field=models.CharField(default='', max_length=30),
        ),
    ]