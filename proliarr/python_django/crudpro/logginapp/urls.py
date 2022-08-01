from django.urls import path
from .views import webpage, login

urlpatterns = [
    path('reg/', webpage),
    path('log/', login)
]