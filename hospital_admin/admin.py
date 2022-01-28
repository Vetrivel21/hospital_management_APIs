from django.contrib import admin

# Register your models here.

from .models import doctor
from .models import patient

admin.site.register(doctor)
admin.site.register(patient)

