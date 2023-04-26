from django.urls import path,include
from .import views
from .views import *


urlpatterns = [
    path('',madhu),
    path('madhu',madhu),
    path('postt',post),
    path('post',firstpost.as_view()),   
]