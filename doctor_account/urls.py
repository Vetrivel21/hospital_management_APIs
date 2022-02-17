#from .views import RegisterAPI
from django.urls import path
from knox import views as knox_views
from .views import LoginAPI
from .views import get_user_data
from .views import RegisterAPI

urlpatterns = [
    path('doctor/register1/', RegisterAPI.as_view(), name='register'),
    path('doctor/login1/', LoginAPI.as_view(), name='login'),
    path('doctor/user1/', get_user_data.as_view(), name='get_user_data'),
    path('doctor/logout1/', knox_views.LogoutView.as_view(), name='logout'),
    path('doctor/logoutall1/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]
