from django.contrib import admin
from django.urls import path, include
from .views import *
from . import views

urlpatterns = [
    path('reg/form/', form.as_view()),
    path('reg/', views.jformat),
    path('reg/list/', views.get_data),
    path('reg/jget/', jgetdata.as_view()),
    path('del/<int:id>', views.delete),
    path('update/<int:id>', views.up_data)

]
