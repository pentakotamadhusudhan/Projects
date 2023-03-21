from django.urls import path

from .views import *


urlpatterns = [
    path('registration',employeeRegistration.as_view()),
    path('get',Employee_get.as_view(), name='get'),
]