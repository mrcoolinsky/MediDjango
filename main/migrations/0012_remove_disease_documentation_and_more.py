# Generated by Django 4.2.7 on 2023-12-11 22:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_remove_documentation_diseases_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='disease',
            name='documentation',
        ),
        migrations.RemoveField(
            model_name='medicine',
            name='documentation',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='documentation',
        ),
        migrations.RemoveField(
            model_name='visit',
            name='documentation',
        ),
        migrations.AlterField(
            model_name='visit',
            name='doctor',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.doctor'),
        ),
        migrations.AlterField(
            model_name='visit',
            name='patient',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.patient'),
        ),
        migrations.DeleteModel(
            name='Documentation',
        ),
    ]
