from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.models import AuthToken
from .serializers import RegisterSerializer
#from .serializers import UserRegisterSerializer


class LoginAPI(APIView):
    def post(self, request):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token = AuthToken.objects.create(user)

        return Response({
            'user_info': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
            },
            'Token': token
        })

class get_user_data(APIView):
    def get(self, request):
        user = request.user

        if user.isauthenticated:
            return Response({
                'user_info': {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                }
            })
        return Response({'error': 'not authenticated'}, status=400)

class RegisterAPI(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save
        token = AuthToken.objects.create(user)

        return Response(
            {
                'user_info': {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                },
                'Token': token
            }
        )

# Create your views here.
