from .views import *
from . import views
from django.urls import path

urlpatterns = [
    path('', views.jformat),
    path('get/ ',views.get_data),
    path('update', views.up_data),
    path('del/<int:id>', views.delete),
    path('update/<int:id>', views.up_data)]
