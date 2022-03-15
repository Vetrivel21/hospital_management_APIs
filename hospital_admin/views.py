from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import doctor
from .models import patient
from .serializers import DoctorSerializer
from .serializers import PatientSerializer
from rest_framework import status
from django.db.models import Q
import math
from django.contrib import admin
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer
from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

class doctor_list(APIView):
    def get(self, request):
        doctors = doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = DoctorSerializer(data=request.data)
        approve = {'Status': 'Approved'}
        if serializer.is_valid():
            serializer.save()
            return Response(approve, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request):
        s = request.GET.get('s')
        f = request.GET.get('f')
        sort = request.GET.get('sort')
        page = int(request.GET.get('page', 1))
        per_page = 32
        doctors = doctor.objects.filter(is_deleted=0).all()

        if s:
            doctors = doctors.filter(Q(name__icontains=s) | Q(email__icontains=s) | Q(specialization__icontains=s))

        if f:
            doctors = doctors.filter(Q(specialization=f))

        if sort == 'asc':
            doctors = doctors.order_by('name')

        elif sort == 'desc':
            doctors = doctors.order_by('-name')

        total = doctors.count()
        start = (page - 1) * per_page
        end = page * per_page
        serializer_class = DoctorSerializer(doctors[start:end], many=True)
        return Response({'data': serializer_class.data,
                         'total': total,
                         'page': page,
                         'last_page': math.ceil(total / per_page),
                         })

class doctor_details(APIView):
    def get(self,request,pk):
        try:
            doctors = doctor.objects.get(pk=pk)
        except doctor.DoesNotExist:
            error = {'status': '400', 'message': 'NOT FOUND'}
            return Response(error, status=status.HTTP_404_NOT_FOUND)
        serializer = DoctorSerializer(doctors)
        return Response(serializer.data)




    def put(self, request,pk):
        try:
            doctors = doctor.objects.get(pk=pk)
        except doctor.DoesNotExist:
            error = {'status': '400', 'message': 'NOT FOUND'}
            return Response(error, status=status.HTTP_404_NOT_FOUND)
        serializer = DoctorSerializer(doctors, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def delete(self, request, pk):
        try:
            doctors = doctor.objects.get(pk=pk)
        except doctor.DoesNotExist:
            error = {'status': '400', 'message': 'NOT FOUND'}
            return Response(error, status=status.HTTP_404_NOT_FOUND)
        doctors.soft_delete()
        reject = {'Status': 'Rejected'}
        return Response(reject, status=status.HTTP_204_NO_CONTENT)
        #data = doctor.objects.filter(is_active=True)

        #return Response(status=status.HTTP_200_OK)





class patient_list(APIView):
    def get(self, request):
        patients = patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PatientSerializer(data=request.data)
        approve = {'Status': 'Approved'}
        if serializer.is_valid():
            serializer.save()
            return Response(approve, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        s = request.GET.get('s')
        f = request.GET.get('f')
        sort = request.GET.get('sort')
        page = int(request.GET.get('page', 1))
        per_page = 32
        patients = patient.objects.filter(is_deleted=0).all()

        if s:
            patients = patients.filter(Q(name__icontains=s) | Q(email__icontains=s))

        if f:
            patients = patients.filter(Q(symptoms=f))

        if sort == 'asc':
            patients = patients.order_by('name')

        elif sort == 'desc':
            patients = patients.order_by('-name')

        total = patients.count()
        start = (page - 1) * per_page
        end = page * per_page
        serializer_class = PatientSerializer(patients[start:end], many=True)
        return Response({'data': serializer_class.data,
                         'total': total,
                         'page': page,
                         'last_page': math.ceil(total / per_page),
                         })

class patient_details(APIView):
    def get(self, request, pk):
        try:
            patients = patient.objects.get(pk=pk)
        except patient.DoesNotExist:
            error = {'status': '400', 'message': 'NOT FOUND'}
            return Response(error, status=status.HTTP_404_NOT_FOUND)
        serializer = PatientSerializer(patients)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            patients = patient.objects.get(pk=pk)
        except patient.DoesNotExist:
            error = {'status': '400', 'message': 'NOT FOUND'}
            return Response(error, status=status.HTTP_404_NOT_FOUND)
        serializer = PatientSerializer(patients, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            patients = patient.objects.get(pk=pk)
        except patient.DoesNotExist:
            error = {'status': '400', 'message': 'NOT FOUND'}
            return Response(error, status=status.HTTP_404_NOT_FOUND)
        patients.soft_delete()
        reject = {'Status': 'Rejected'}
        return Response(reject, status=status.HTTP_204_NO_CONTENT)


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1],
        })


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)

