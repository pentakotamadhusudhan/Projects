from django.urls import path
from .views import *

urlpatterns = [
     path('form1/', funone.as_view()),
     path('form2/', funtwo.as_view()),
     #path('form3',form3view.as_view()),
     path('GetModel/', GetModel.as_view()),
]