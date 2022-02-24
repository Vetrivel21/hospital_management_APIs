from .views import RegisterAPI
from django.urls import path
from knox import views as knox_views
from .views import LoginAPI
from .views import user_information

urlpatterns = [
    path('doctor/register/', RegisterAPI.as_view(), name='register'),
    path('doctor/login/', LoginAPI.as_view(), name='login'),
    path('doctor/user/', user_information.as_view(), name='user'),
]
