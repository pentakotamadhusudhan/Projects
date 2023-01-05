from django.urls import path
from . import views
from .views import loginview
urlpatterns = [
    path('',loginview.as_view()),
]