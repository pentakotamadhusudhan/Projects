from .models import resetmodel
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response

from .serializers import resetserializer, regserializer, loginserializer


# Create your views here.
class resetview(generics.CreateAPIView):
    serializer_class = regserializer

    #


class resetpassword(generics.UpdateAPIView):
    serializer_class = resetserializer
    queryset = resetmodel.objects.all()

    def post(self, request):
        email = request.data.get('email')
        new_password = request.data.get('new_password')
        re_type_password = request.data.get('re_type_password')
        user = resetmodel.objects.get(email=email)
        if new_password == re_type_password:
            n = resetmodel.objects.get(email=email)
            user.password = re_type_password
            user.save()
            return Response(regserializer(n).data)
        else:
            return Response({"new_password": ["new password and re-type password must be same"]})


class login(generics.GenericAPIView):
    serializer_class = loginserializer

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = resetmodel.objects.get(username=username)
        if username == user.password and username == user.username:
            user = loginserializer(data=request.data)
            user.save()
            return Response('login success')
        else:
            return Response('password or username is invalid')
