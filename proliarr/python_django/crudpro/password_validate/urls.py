from django.urls import path
from .views import validateview

urlpatterns = [
    path('',validateview.as_view())
]