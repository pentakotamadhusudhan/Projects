from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from .models import *
from .serializer import studentserializer, employeeserializer, peopleserializer


# Create your views here.
class studentview(generics.CreateAPIView):
    serializer_class = studentserializer


class employeeview(generics.GenericAPIView):
    serializer_class = employeeserializer

    def post(self, request):
        name = self.get_serializer(data=request.data)
        name.is_valid(raise_exception=True)
        user = name.save()
        return Response(employeeserializer(user).data)


class peopleview(generics.GenericAPIView):
    serializer_class = peopleserializer

    def post(self, request):
        Name = self.get_serializer(data=request.data)
        Name.is_valid(raise_exception=True)
        user = Name.save()
        return Response(peopleserializer(user).data)



class getstudent(generics.ListAPIView):
    queryset = studentmodel.objects.all()
    serializer_class = studentserializer


class getemployee(generics.ListAPIView):
    queryset = employeemodel.objects.all()
    serializer_class = employeeserializer


class getpeople(generics.ListAPIView):
    queryset = peoplemodel.objects.all()
    serializer_class = peopleserializer
