from django.urls import path
from .views import RegisterAPI,LoginAPI

urlpatterns = [
    path('api',RegisterAPI.as_view()),
    path('api/login/', LoginAPI.as_view(), name='login'),
    ]