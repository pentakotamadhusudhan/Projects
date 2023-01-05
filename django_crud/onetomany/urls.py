from django.urls import path
from .views import *
urlpatterns=[
    path('main',mainpage.as_view()),
    path('next',nextpage.as_view()),
    path('get',getform.as_view())
]
