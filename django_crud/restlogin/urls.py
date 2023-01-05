from django.urls import path,include
from .views import regview,reg2,regvalidate,loginview
urlpatterns = [
    path('2',reg2.as_view()),
    path('',regview.as_view()),
    path('login',loginview.as_view())
]