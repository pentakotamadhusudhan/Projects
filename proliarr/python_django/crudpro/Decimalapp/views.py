from django.shortcuts import render
from rest_framework.response import Response

from .serializers import decimalserializer,retrieveserializer
from .models import Decimalmodel
from rest_framework import generics


# Create your views here.
class Decimalview(generics.GenericAPIView):
    serializer_class = decimalserializer

    def post(self,request):
        ser=decimalserializer(data=request.data)
        ser.is_valid()
        user=ser.save()
        return Response(retrieveserializer(user).data)