# Generated by Django 3.2.10 on 2022-02-23 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor_information', '0004_alter_account_managers'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='email',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]