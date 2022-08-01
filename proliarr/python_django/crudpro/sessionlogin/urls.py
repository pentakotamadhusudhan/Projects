from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login),
    path('time', views.time),
    path('logout', views.logout)
]
