from django.urls import path
from .views import bmiview

urlpatterns = [
    path('', bmiview.as_view())
]
