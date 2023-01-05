from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import bmimodel
from .serializers import bmiserializer, showserializer


# Create your views here.


class bmiview(generics.GenericAPIView):
    class bmiView(generics.GenericAPIView):
        serializer_class = bmiserializer

        def post(self, request):
            height = request.data.get('height')
            weight = request.data.get('weight')
            height = int(height)
            weight = int(weight)
            bmi = weight / (height / 100) ** 2
            round_bmi = round(bmi, 2)
            ob = bmimodel()
            ob.height = height
            ob.weight = weight
            ob.bmi = round_bmi
            ob.save()
            return Response(showserializer(ob).data)
