from django.shortcuts import render
from .serializers import *
from rest_framework.response import Response
from rest_framework import generics


class convertdob(generics.GenericAPIView):
    serializer_class = converterserializer

    def post(self, request, *args, **kwargs):
        form = converterserializer(data=request.data)
        print(form)

        form.is_valid()
        user = form.save()
        return Response(dataserializer(user).data)
