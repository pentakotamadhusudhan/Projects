from django.urls import path
from .views import formview
urlpatterns = [
    path('',formview.as_view())
]