from django.shortcuts import render
from .serializers import *
from rest_framework import generics
from rest_framework.response import Response


class Diffdate(generics.GenericAPIView):
    serializer_class = converterserializer

    def post(self, request, *arges, **kwargs):
        form = converterserializer(data=request.data)
        print(form)
        form.is_valid()
        user = form.save()
        return Response(dataserializer(user).data)
