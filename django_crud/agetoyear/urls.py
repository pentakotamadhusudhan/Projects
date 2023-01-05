from django.urls import path
from .views import *

urlpatterns = [
    path('', reverse.as_view())
]
