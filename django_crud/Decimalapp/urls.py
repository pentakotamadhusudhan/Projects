from django.urls import path
from .views import Decimalview

urlpatterns = [
    path('',Decimalview.as_view())
]
