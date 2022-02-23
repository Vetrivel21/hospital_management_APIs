from django.db import models


# Create your models here.

class account(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100, blank=True)



