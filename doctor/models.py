from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager

# Create your models here.

class doctor_account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    address = models.TextField(blank=True)
    mobile_no = models.IntegerField(blank=True)
    specialization = models.CharField(max_length=60, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    objects = UserManager()
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError("Enter a valid email address.")
        if not username:
            raise ValueError("Enter a valid email username.")
        user = self.model(
            email=self.normalize_email(email),
            username = username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


