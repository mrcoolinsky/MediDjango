# Generated by Django 4.2.7 on 2023-12-10 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_visit_diseases_visit_medicines'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine',
            name='dosage',
            field=models.CharField(default='', max_length=10),
        ),
    ]
