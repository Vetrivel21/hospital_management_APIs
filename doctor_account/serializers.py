from rest_framework import serializers, validators
from django.contrib.auth.models import User
#from djoser.serializers import UserCreateSerializer as BaseUserRegisterSerializer


# User Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email')
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {
                "required": True,
                "validators": [
                    validators.UniqueValidator(
                        User.objects.all(), "A user with that email already exists")
                ]
            }
        }

    def create(self, validated_data):
        username = validated_data.get('username')
        password = validated_data.get('password')
        email = validated_data.get('email')
        #address = validated_data.get('address')
        #mobile_no = validated_data.get('mobile_no')
        #specialization = validated_data.get('specialization')

        user = User.objects.create(
            username = username,
            password = password,
            email = email,
            #address = address,
            #mobile_no = mobile_no,
            #specialization = specialization,
        )

        return user
