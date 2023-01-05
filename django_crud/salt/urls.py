from django.urls import path
from .import views
from .views import regview,get_data,login
urlpatterns = [
    path('',regview.as_view()),
    path('/get',get_data.as_view()),
    path('/login',login.as_view())
]