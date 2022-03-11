from rest_framework import serializers
from django.contrib.auth.models import User
from hospital_admin.models import doctor


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = doctor
        fields = "__all__"
        extra_kwargs = {'password': {'write_only': True}}

    '''def create(self, validated_data):
        user = doctor.objects.create_user(validated_data['name'], validated_data['passowrd'])

        return user'''

'''class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'password')'''

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = doctor
        fields = ('username', 'password')

    '''def create(self, validated_data):
        user = doctor.objects.create_user(validated_data['name'], validated_data['password'])

        return user'''



