from django.contrib import admin
from django.urls import path, include
from .views import *
from . import views

urlpatterns = [
    path('',loginrfw.as_view()),
    path('form',loginform.as_view()),
    path('logout',views.logout)
]
