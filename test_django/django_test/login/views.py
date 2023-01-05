from rest_framework import generics
from rest_framework.response import Response

from .seriliazers import *
from django.shortcuts import render
# from test_django.django_test.crud.models import employee
from django.apps import apps
# Create your views here.
class loginview(generics.GenericAPIView):
    serializer_class = loginseriliazer

    def post(self,request):
        user = request.data.get('name')
        password = request.data.get('password')
        empmodel = apps.get_model('crud','employee')
        if empmodel.objects.get(name= user):
            emp=empmodel.objects.get(name= user)
        else:
            return Response('username details is not avaliable')
        if emp.password == password:
            return Response('login successs')
        else:
            return Response('login failed')


