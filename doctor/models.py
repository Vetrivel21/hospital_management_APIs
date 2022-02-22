from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.contrib.auth.models import AbstractUser
#from django.utils import timezone
# Create your models here.

class doctor_account(AbstractBaseUser):
    username = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=300, default='')
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    address = models.TextField(blank=True)
    mobile_no = models.IntegerField(default=0, blank=True)
    specialization = models.CharField(max_length=60, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True, null=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now_add=True, null=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    #is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    #hide_email = models.BooleanField(default=True)


    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'address', 'password', 'mobile_no', 'specialization']

    '''def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True'''

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




