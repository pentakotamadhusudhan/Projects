from django.shortcuts import render
from .models import form
from .serializers import formserializer
from rest_framework import generics
# Create your views here.
class formview(generics.DestroyAPIView):
    serializer_class = formserializer