from .views import RegisterAPI
from django.urls import path
from knox import views as knox_views
from .views import LoginAPI



urlpatterns = [
    path('doctor/register/', RegisterAPI.as_view(), name='register'),
    path('doctor/login/', LoginAPI.as_view(), name ='login'),


]
