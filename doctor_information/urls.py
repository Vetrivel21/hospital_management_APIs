from .views import RegisterAPI
from django.urls import path
from knox import views as knox_views



urlpatterns = [
    path('doctor/register/', RegisterAPI.as_view(), name='register'),
   
]
