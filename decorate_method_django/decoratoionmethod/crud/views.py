from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework import generics
from django.contrib.auth.models import User
from django.shortcuts import render
from .serializers import firstser

# Create your views here.


def madhu(request):
    if request.method=="POST":
        print('madhu')
        # return render(request,'registrer.html')
    return render(request,"index.html")


@api_view(['POST'])
def post(request):
    ser = firstser(data=request.data)
    if ser.is_valid(raise_exception=True):
        ser.save()
        return render(request,"registrer.html",{"dataa":ser})
    





class firstpost(generics.GenericAPIView):
    serializer_class = firstser
    def post(self,request):
        ser = firstser(data=request.data)
        ser.is_valid()
        ser.save()
        return render(request,"registrer.html",{"dataa":ser})
    

