from django.urls import path

from .import views
urlpatterns=[
    path('page1',views.regi),
    path('student',views.studentreg),
    path('emp',views.employeereg),
    path('cat',views.categeory),
    path('login',views.login),
    path('stu',views.studentlogin),
    path('emplogin',views.employeelogin),
    path('etime',views.emptime),
    path('stime',views.stutime),
    path('time',views.time)
]