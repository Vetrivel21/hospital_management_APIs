from rest_framework import serializers
from django.contrib.auth.models import User
from hospital_admin.models import doctor


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = doctor
        fields = "__all__"
        extra_kwargs = {'password': {'write_only': True}}


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = doctor
        fields = ('username', 'password')

  

