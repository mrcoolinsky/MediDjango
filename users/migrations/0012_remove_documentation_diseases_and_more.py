# Generated by Django 4.2.7 on 2023-11-15 22:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_alter_documentation_diseases_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documentation',
            name='diseases',
        ),
        migrations.RemoveField(
            model_name='documentation',
            name='medicines',
        ),
        migrations.RemoveField(
            model_name='documentation',
            name='visits',
        ),
        migrations.AddField(
            model_name='documentation',
            name='diseases',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.disease'),
        ),
        migrations.AddField(
            model_name='documentation',
            name='medicines',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.medicine'),
        ),
        migrations.AddField(
            model_name='documentation',
            name='visits',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.visit'),
        ),
    ]
