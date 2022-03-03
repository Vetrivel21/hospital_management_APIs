from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, Register_apiSerializer
from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from .models import account
from .models import user_details
from rest_framework import status
from rest_framework.views import APIView
from django.core.mail import send_mail
from .serializers import LoginSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

class user_information_registerAPI(APIView):
    def post(self, request):
        doctor_details = user_details.objects.all()
        serializer = UserSerializer(doctor_details, many=True)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            send_mail(
                'Doctor details',
                 f'{serializer.data}',
                'fromljh59591@qopow.com',
                ['tovetrisenthilmkce@gmail.com'],
                fail_silently=False,
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegisterAPI(generics.GenericAPIView):
    def post(self, request):
        doctor_credentials = account.objects.all()
        serializer = Register_apiSerializer(doctor_credentials, many=True)
        serializer = Register_apiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            send_mail(
                'Doctor credentials',
                f'{serializer.data}',
                'fromvetrisenthilmkce@gmail.com',
                ['tovetrisenthilmkce@gmail.com'],
                fail_silently=False,
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            '''subject = 'welcome to GFG world'
            message = f'Hi {user.username}, thank you for registering in geeksforgeeks.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ['tovetrisenthilmkce@gmail.com']
            send_mail(subject, message, email_from, recipient_list)'''
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                #"user": UserSerializer(user, context=self.get_serializer_context()).data,
                #"token": AuthToken.objects.create(user)[1],




'''class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        #doctor_details = account.objects.all()
        #serializer = UserSerializer(doctor_details, many=True)
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)'''

'''class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = LoginSerializer
    queryset = get_user_model().objects.all()'''

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        doctor_login = account.objects.all()
        serializer = LoginSerializer(doctor_login, many=True)
        serializer = AuthTokenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            login(request, user)
            return super(LoginAPI, self).post(request, format=None)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
