# Generated by Django 4.2.7 on 2023-12-28 23:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_alter_dosage_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='disease',
            old_name='property',
            new_name='symptoms',
        ),
    ]
