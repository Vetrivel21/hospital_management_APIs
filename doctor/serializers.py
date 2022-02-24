from rest_framework import serializers, validators
from django.contrib.auth.models import User
from .models import account
# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = account
        fields = "__all__"

    def create(self, validated_data):
            user = account.objects.create_user(validated_data['username'], validated_data['password'])

            return user

# Register Serializer
class Register_apiSerializer(serializers.ModelSerializer):
    class Meta:
        model = account
        fields = "__all__"
        #fields = ('id', 'username', 'email')
        '''extra_kwargs = {'password': {'write_only': True}}'''

    '''def create(self, validated_data):
        user = account.objects.create_user(self.validated_data['username'], password=self.validated_data['password'])

        return user'''
