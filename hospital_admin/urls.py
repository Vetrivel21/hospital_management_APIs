from django.urls import path
from .import views
from .views import RegisterAPI
from django.urls import path
from knox import views as knox_views
from .views import LoginAPI

urlpatterns=[
    path('doctor/', views.doctor_list.as_view(), name='doctor-list'),
    path('patient/', views.patient_list.as_view(), name='patient-list'),
    path('doctor/<int:pk>/', views.doctor_details.as_view(), name='doctor-details'),
    path('patient/<int:pk>/', views.patient_details.as_view(), name='patient-details'),
    path('admin/register/', RegisterAPI.as_view(), name='register'),
    path('admin/login/', LoginAPI.as_view(), name='login'),
    path('admin/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('admin/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),

]

