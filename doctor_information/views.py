from rest_framework.views import APIView
from rest_framework.response import Response
from .models import doctor_details
from .serializers import RegisterSerializer
from rest_framework import status
from knox.models import AuthToken
from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from django.core.mail import send_mail

class RegisterAPI(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            send_mail(
                'Doctor credentials',
                f'{serializer.data}',
                'fromsenthil123@gmail.com',
                ['tovetrisenthilmkce@gmail.com'],
                fail_silently=False,
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

