from rest_framework import serializers, validators
from django.contrib.auth.models import User
from .models import doctor_account
# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = doctor_account
        fields = "__all__"

# Register Serializer
class Register_apiSerializer(serializers.ModelSerializer):
    class Meta:
        model = doctor_account
        fields = "__all__"
        #fields = ('id', 'username', 'email')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = doctor_account.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user
