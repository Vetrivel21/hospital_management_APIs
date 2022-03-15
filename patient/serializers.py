from rest_framework import serializers
from hospital_admin.models import patient

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = patient
        fields = "__all__"
        extra_kwargs = {'password': {'write_only': True}}

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = patient
        fields = ('username', 'password')
