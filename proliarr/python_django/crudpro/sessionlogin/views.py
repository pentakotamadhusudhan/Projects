from django.http import HttpResponse
from django.shortcuts import render
from CRUD.models import *
from sessionlogin.get import time


# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST['name']
        Password = request.POST['password']
        user = Details.objects.get(name=username)  # Details is model name
        request.session['name'] = user.name  # we get with the name refernce
        if Password == user.password:
            pass
        else:
            return HttpResponse('invalid password')

    return render(request, 'log.html')


def time(request):  # this fun is for track the login session

    if 'name' in request.session:
        ver = request.session['name']
        return HttpResponse('login success')
    else:
        return HttpResponse('session expiry')


def logout(request):
    Queryset = Details.objects.all()
    try:
        del Queryset.session['name']
    except:
        return render(request, 'index.html')
    return render(request, 'index.html')
