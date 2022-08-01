from django.urls import path
from .views import *

urlpatterns = [
    path('', convertdob.as_view())
]
