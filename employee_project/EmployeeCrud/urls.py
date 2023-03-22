from django.urls import path

from .views import *
from .Crud.Employee_delete import *


urlpatterns = [
    path('employeeRegistration',employeeRegistration.as_view()),
    path('get',Employee_get.as_view(), name='get'),
    path('project/',projectmodel_view().as_view(), name='post'),
    path('work/',workingview().as_view(), name='post'),
    path('qualification/',qualificationview().as_view(), name='post'),
    path('employeeUpdate/<str:regId>/',Updateview().as_view(), name='put'),
    path('workUpdate/<str:regId>/',workUpdateview().as_view(), name='put'),
    path('qualificationUpdate/<str:regId>/',qualificationupdateview().as_view(), name='put'),
    path('projectUpdate/<str:regId>/',projectupdateview().as_view(), name='put'),
    path('delete/<str:regId>',Employee_delete().as_view(), name='put'),
]