from django.urls import path
from .views import doctor_list
from .views import patient_list
from .views import doctor_details
from .views import patient_details
from .views import dischargeAPI
from .views import RegisterAPI
from django.urls import path
from knox import views as knox_views
from .views import LoginAPI
#from .views import admin_login


urlpatterns=[
    path('doctor/', doctor_list.as_view(), name='doctor-list'),
    path('patient/', patient_list.as_view(), name='patient-list'),
    path('doctor/<int:pk>/', doctor_details.as_view(), name='doctor-details'),
    path('patient/<int:pk>/', patient_details.as_view(), name='patient-details'),
    path('patient/discharge/', dischargeAPI.as_view(), name='discharge'),
    path('admin/register/', RegisterAPI.as_view(), name='register'),
    path('admin/login/', LoginAPI.as_view(), name='login'),
    path('admin/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('admin/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    #path('admin/login/', admin_login.as_view(), name='login'),



]

