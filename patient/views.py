from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer
from rest_framework import status
from hospital_admin.models import patient
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from .serializers import LoginSerializer

class RegisterAPI(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            send_mail(
                'Doctor credentials',
                f'{serializer.data}',
                'from{email}',
                ['tovetrisenthilmkce@gmail.com'],
                fail_silently=False,
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginAPI(APIView):

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(username = request.data.get('username'), password = request.data.get('password'))
            if user is not None:
                login(request, user)
                response = {'You have successfully logged in.'}
                return Response(response, status=status.HTTP_200_OK)
            else:
                return Response({'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
