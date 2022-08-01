from django.urls import path
from .views import resetview,resetpassword,login
urlpatterns =[
    path('',resetview.as_view()),
    path('re',resetpassword.as_view()),
    path('login',login.as_view())
]
