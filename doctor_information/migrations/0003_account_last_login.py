# Generated by Django 3.2.10 on 2022-02-23 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor_information', '0002_auto_20220223_1826'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
    ]
