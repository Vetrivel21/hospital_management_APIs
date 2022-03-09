from django.db import models


# Create your models here.
'''class SoftDeleteManager(models.Manager):

    def get_queryset(self, *args, **kwargs):
        return super(SoftDeleteManager, self).get_queryset(*args, **kwargs).filter(is_active=True)

    def everything(self, *args, **kwargs):
        return super(SoftDeleteManager, self).get_queryset(*args, **kwargs)'''

class doctor(models.Model):
    name = models.CharField(max_length=200, blank=True)
    email = models.CharField(max_length=200, blank=True)
    address = models.TextField(blank=True)
    mobile_no = models.IntegerField(null=True)
    specialization = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    is_deleted = models.BooleanField(default=False)

    def soft_delete(self):
        self.is_deleted = True
        self.save()

class patient(models.Model):
    name = models.CharField(max_length=200, blank=True)
    email = models.CharField(max_length=200, blank=True)
    address = models.TextField(blank=True)
    mobile_no = models.IntegerField(null=True)
    symptoms = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    is_deleted = models.BooleanField(default=False)

    def soft_delete(self):
        self.is_deleted = True
        self.save()

    def __str__(self):
        return self.name



