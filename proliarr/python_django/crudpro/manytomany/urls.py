from django.urls import path
from .views import *

urlpatterns = [
    path('stu',studentview.as_view()),
    path('emp',employeeview.as_view()),
    path('',peopleview.as_view()),
    path('gets',getstudent.as_view()),
    path('gete',getemployee.as_view()),
    path('getp',getpeople.as_view())


]
