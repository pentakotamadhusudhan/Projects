from django.contrib.auth.hashers import check_password
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from .serializers import regserilizer, getserilizer, logserilizer
from .models import saltmodel


# Create your views here.
class regview(generics.GenericAPIView):
    serializer_class = regserilizer

    def post(self, request):
        ser = regserilizer(data=request.data)
        ser.is_valid(raise_exception=True)
        user = ser.save()
        return Response(regserilizer(user).data)


class get_data(generics.ListAPIView):
    queryset = saltmodel.objects.all()
    serializer_class = getserilizer


class login(generics.GenericAPIView):
    serializer_class = logserilizer

    def post(self, request):
        Name = request.data.get('name')
        password = request.data.get('passwpord')
        user = saltmodel.objects.get(name=Name)
        if check_password(password, user.password):
            ser = logserilizer(data=request.data)
            ser.save()
        return Response(regserilizer(user).data)
