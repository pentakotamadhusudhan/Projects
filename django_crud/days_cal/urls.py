from django.urls import path
from .views import *


urlpatterns = [
    path('diff/',Diffdate.as_view())
]

