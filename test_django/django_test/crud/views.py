from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, request
from rest_framework import generics
from .models import employee
from .serializers import *


# creating CRUD operations using rest_crud framework
# its we have to enter the data as json formate.
class regview(generics.GenericAPIView):
    serializer_class = classSerializer
    def post(self,request):
        ser = classSerializer(data=request.data)
        employee.objects.create(name='Madhu',department='EEE',password='1245')

        if ser.is_valid():
            ser.save()
        return Response(ser.data)


# here its like form

class form(generics.CreateAPIView):
    serializer_class = classSerializer

    def post(self,request):
        ser = classSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
        return Response()


@api_view(['POST'])
def up_data(request, id):
    emp = employee.objects.get(id=id)
    s = classSerializer(instance=emp, data=request.data)
    if s.is_valid():
        s.save()
    return Response(s.data)


@api_view(['GET'])
def get_data(request):
    employee_ob = employee.objects.all()
    serializer = classSerializer(employee_ob, many=True)
    return Response(serializer.data)


class jgetdata(generics.ListAPIView):
    queryset = employee.objects.all()
    serializer_class = classSerializer


@api_view(['delete'])
def delete(request, id):
    emp_obj = employee.objects.get(id=id)
    emp_obj.delete()
    return Response('employee ')