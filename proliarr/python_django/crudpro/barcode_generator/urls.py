from django.urls import path
from .views import *
urlpatterns = [
    path('',barview.as_view()),
    path('read',barreadView.as_view())
]