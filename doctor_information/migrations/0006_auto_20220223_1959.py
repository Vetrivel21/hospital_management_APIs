# Generated by Django 3.2.10 on 2022-02-23 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor_information', '0005_account_email'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='account',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='account',
            name='email',
        ),
        migrations.RemoveField(
            model_name='account',
            name='last_login',
        ),
    ]