# Generated by Django 4.2.7 on 2023-11-15 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_documentation_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentation',
            name='diseases',
            field=models.ManyToManyField(null=True, to='users.disease'),
        ),
        migrations.AlterField(
            model_name='documentation',
            name='medicines',
            field=models.ManyToManyField(null=True, to='users.medicine'),
        ),
        migrations.AlterField(
            model_name='documentation',
            name='visits',
            field=models.ManyToManyField(null=True, to='users.visit'),
        ),
    ]
