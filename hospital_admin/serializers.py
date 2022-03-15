from rest_framework import serializers
from .models import doctor
from .models import patient
from rest_framework import serializers, validators
from django.contrib.auth.models import User

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = doctor
        fields = "__all__"

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = patient
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user
