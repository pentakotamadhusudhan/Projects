from rest_framework import generics

from rest_framework.response import Response
from .serializers import *
from django.shortcuts import render
from .models import *


class funone(generics.GenericAPIView):
    serializer_class = form1serializer

    def post(self, request, *args, **kwargs):
        a = form1serializer(data=request.data)

        a.is_valid()
        user = a.save()
        return Response(form1serializer(user).data)


class funtwo(generics.GenericAPIView):
    serializer_class = form2serializer

    def post(self, request, *args, **kwargs):
        b = form2serializer(data=request.data)
        b.is_valid(raise_exception=True)
        user = b.save()
        return Response(form2serializer(user).data)



class GetModel(generics.GenericAPIView):
    queryset = form2serializer

    def get(self, request):
        m = main3.objects.all()
        ser = form2serializer(m, many=True)

        return Response(ser.data)
