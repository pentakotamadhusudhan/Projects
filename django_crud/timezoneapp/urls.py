from django.urls import path
from .views import *
urlpatterns = [
    path('',timeview.as_view())
]