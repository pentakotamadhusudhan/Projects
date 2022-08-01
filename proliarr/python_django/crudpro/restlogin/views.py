from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, status
from .serializers import loginserializer, passwordserializer
from .models import logintable
from rest_framework import generics


# Create your views here.

def valid(request):
    a = logintable()
    a.first_name = request.data.get('first_name')
    a.second_name = request.data.get('second_name')
    a.username = request.data.get('username')
    a.password = request.data.get('password')
    a.email = request.data.get('email')
    a.gender = request.data.get('gender')
    a.datetime = request.data.get('datetime')
    a.save()


def fun(n):
    for i in n:
        if i.isupper() == True:
            global u
            u = True
            break

    for i in n:
        if i.islower() == True:
            global l
            l = True
            break
    for i in n:
        if i.isdigit() == True:
            global d
            d = True
            break
    for i in n:
        if i in ('@', '#', '$', '%', '^', '&', '*'):
            global y
            y = True
            break
    if u == True and y == True and d == True and l == True:
        global s
        s = True
    else:
        s=False
    return None


class regview(generics.GenericAPIView):
    serializer_class = loginserializer

    def post(self, request):

        Password = request.data.get('password')
        fun(Password)
        if s==True:
            ser = loginserializer(data=request.data)
            ser.is_valid()
            ser.save()
            return Response(ser.data)
        elif s==False:
            return HttpResponse('password is in valid')



class reg2(generics.GenericAPIView):
    serializer_class = loginserializer

    def post(self, request):
        ser = loginserializer(data=request.data)
        ser.is_valid()
        user = ser.save()
        return Response(loginserializer(user).data)


class regvalidate(viewsets.ModelViewSet):
    queryset = logintable.objects.all()
    serializer_class = loginserializer

    @action(detail=True, methods=['post'])
    def set_password(self, request):
        user = self.get_object()
        serializer = passwordserializer(data=request.data)
        if serializer.is_valid():
            user.set_password(serializer.validated_data['password'])
            user.save()
            return Response({'status': 'password set'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_BAD_REQUEST)


class loginview(generics.GenericAPIView):
    serializer_class = passwordserializer

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = logintable.objects.get(username=username)
        if username == user.password:
            user = loginserializer(data=request.data)
            user.save()
        return Response(loginserializer(user).data)
