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
from rest_framework import status
from rest_framework.views import APIView
from django.core.mail import send_mail

class user_information(APIView):
    def post(self, request):
        send_mail(
            'Doctor details',
            'Name: Sivan, email: sivan@gmail.com, address: 524/1, Jawahar Bazaar, Karur., mobileno: 2134567854, specialization: M.D.',
            'fromkavithaswaminathan@gmail.com',
            ['tovetrisenthilmkce@gmail.com'],
            fail_silently=False,
        )


class RegisterAPI(generics.GenericAPIView):
    def post(self, request):
        doctor_details = account.objects.all()
        serializer = Register_apiSerializer(doctor_details, many=True)
        serializer = Register_apiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            send_mail(
                'Doctor details',
                'username, password',
                'fromvetrisenthilmkce@gmail.com',
                ['tokavithaswaminathan433@gmail.com'],
                fail_silently=False,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                #"user": UserSerializer(user, context=self.get_serializer_context()).data,
                #"token": AuthToken.objects.create(user)[1],




class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        doctor_details = account.objects.all()
        serializer = UserSerializer(doctor_details, many=True)
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)
