from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from .serializers import *


# Create your views here.
class mainpage(generics.CreateAPIView):
    serializer_class = mainserializer


class nextpage(generics.CreateAPIView):
    serializer_class = nextserializer

    def post(self, request, *args, **kwargs):
        b = nextserializer(data=request.data)
        b.is_valid(raise_exception=True)
        user = b.save()
        return Response(nextserializer(user).data)

class getform(generics.ListAPIView):
    queryset = nextserializer


    def post(self, request):
        details = nextform.objects.all()
        det=main.objects.all()
        serializer = nextserializer(details, many=True)
        ser=mainserializer(det,many=True)
        print(serializer.data)
        return Response(ser.data)