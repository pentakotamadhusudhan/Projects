from django.shortcuts import render, redirect
from .models import Details
from django.http import HttpResponse
import datetime


# creating CRUD operations ,and login
# Create your views here.
def index(request):
    current_time = datetime.datetime.now()

    return render(request, 'index.html', {'current_time': current_time})


def create(request):
    """u r successfully login"""

    if request.method == "POST":
        a = Details()
        a.name = request.POST['name']
        a.time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        a.age = request.POST['age']
        a.address = request.POST['address']
        a.password = request.POST['password']

        a.save()
    return render(request, 'index.html')


def update(request, id):
    ob = Details.objects.get(id=id)
    if request.method == "POST":
        ob.name = request.POST.get('name')
        ob.age = request.POST.get('age')
        ob.address = request.POST.get('address')
        ob.password = request.POST.get('password')
        ob.save()
    return render(request, 'update.html', {'Details': ob})


def retrieve(request):
    details = Details.objects.all()
    return render(request, 'retrieve.html', {'Details': details})


def delete(request, id):
    a = Details.objects.get(id=id)
    a.delete()
    return redirect('/retrieve')


def login(request):
    if request.method == "POST":
        username = request.POST['name']
        Password = request.POST['password']
        user = Details.objects.get(name=username)
        if Password == user.password:
            return render(request, 'index.html')
        else:
            return HttpResponse('invalid password')

    return render(request, 'log.html')
