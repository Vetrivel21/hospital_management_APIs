from rest_framework import serializers
from .models import doctor_details
from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = doctor_details
        fields = "__all__"



