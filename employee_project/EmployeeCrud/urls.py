from django.urls import path

from .views import *
from .Crud.Employee_delete import *


urlpatterns = [
    path('employeeRegistration',employeeRegistration.as_view()),
    path('get',Employee_get.as_view(), name='get'),
    path('project/',projectmodel_view().as_view(), name='post'),
    path('work/',workingview().as_view(), name='post'),
    path('qualification/',qualificationview().as_view(), name='post'),
    path('employeeUpdate/<str:EmpId>/',Updateview().as_view(), name='put'),
    path('workUpdate/<str:EmpId>/',workUpdateview().as_view(), name='put'),
    path('qualificationUpdate/<str:EmpId>/',qualificationupdateview().as_view(), name='put'),
    path('projectUpdate/<str:EmpId>/',projectupdateview().as_view(), name='put'),
    path('delete/<str:Empid>',Employee_delete().as_view(), name='put'),
]