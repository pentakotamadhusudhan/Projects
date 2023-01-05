from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import barmodel
from .serializers import barserializer, retrieveserializer


# Create your views here.
class barview(generics.GenericAPIView):
    serializer_class = barserializer

    def post(self, request):
        ser = barserializer(data=request.data)
        ser.is_valid()
        user = ser.save()
        return Response(barserializer(user).data)


class barreadView(generics.GenericAPIView):
    serializer_class = retrieveserializer

    def post(self, request):
        file = request.FILES['image_field']
        print(file)

