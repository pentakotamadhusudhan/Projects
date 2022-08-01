from django.contrib.auth.hashers import check_password
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, request
# creating login ang registrations using rest_crud framework
from CRUD.models import Details
from rest_crud.models import employee
from .serializers import loginSerializer, classSerializer
from django.http import HttpResponse


class loginform(generics.CreateAPIView):
    serializer_class = classSerializer

    def post(self, request):
        ser = classSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
        return Response(ser.data)


class loginrfw(generics.GenericAPIView):
    serializer_class = loginSerializer

    def post(self, request):
        Name = request.data.get('name')
        password = request.data.get('password')
        userdata = employee.objects.get(name=Name)
        if check_password(password, userdata.password):
            user = loginSerializer(data=request.data)
            user.save()
        return Response(classSerializer(userdata).data)


'''

class loginrfw(generics.GenericAPIView):
    serializer_class = loginSerializer

    def post(self, request):
        Name = request.data.get('name')
        password = request.data.get('password')
        userdata = employee.objects.get(name=Name)
        if password==userdata.password:
            user = loginSerializer(data=request.data)
            user.save()
        return Response(classSerializer(userdata).data)

'''


def logout(requests):
    queryset = employee.objects.all()
    try:
        del queryset.session['name']
    except:
        return HttpResponse('logout success')
    # return render(request, 'index.html')
