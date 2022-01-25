from django.db import models

# Create your models here.
class doctor(models.Model):
    name = models.CharField(max_length=200, blank=True)
    email = models.CharField(max_length=100, blank=True)
    address = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)

class patient(models.Model):
    name = models.CharField(max_length=200, blank=True)
    email = models.CharField(max_length=100, blank=True)
    address = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


