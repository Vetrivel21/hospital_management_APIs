from django.db import models


# Create your models here.

class account(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100, blank=True)

class user_details(models.Model):
    name = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    address = models.TextField(blank=True)
    mobile_no = models.CharField(max_length=14, blank=True)
    specialization = models.CharField(max_length=50, blank=True)



