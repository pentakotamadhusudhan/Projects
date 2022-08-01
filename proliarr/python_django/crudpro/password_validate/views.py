from django.shortcuts import render
from rest_framework.response import Response

from .serializers import validateserializer
from rest_framework import generics
# Create your views here.
class validateview(generics.GenericAPIView):
    serializer_class = validateserializer

    def post(self, request):
        detail = self.get_serializer(data=request.data)
        detail.is_valid(raise_exception=True)
        user = detail.save()
        return Response(validateserializer(user).data)