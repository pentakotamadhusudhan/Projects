import requests
from django.shortcuts import render
from .models import pagemodel, student, employee
from django.http import HttpResponse


# Create your views here.
def regi(request):
    if request.method == 'POST':
        a = pagemodel()
        a.name = request.POST['name']
        a.surname = request.POST['surname']
        a.password = request.POST['password']
        a.save()
        return HttpResponse('saved the data')
    return render(request, 'page1.html')


def studentreg(request):
    if request.method == 'POST':
        a = student()
        a.student_id = request.POST['student_id']
        a.student_name = request.POST['student_name']
        a.password = request.POST['password']
        a.save()
        return HttpResponse('saved the data')
    return render(request, 'student.html')


def employeereg(request):
    if request.method == 'POST':
        a = employee()
        a.emp_name = request.POST['emp_name']
        a.emp_age = request.POST['emp_age']
        a.password = request.POST['password']
        a.save()
        return HttpResponse('saved the data')
    return render(request, 'employee.html')

def categeory(request):
    if request.method=='POST':
        global categeory
        catageory=request.POST['categeory']
        return HttpResponse('madhu')

    return render(request,'log.html')



def login(request):
    if request.method == "POST":
        try:
            Userdetails = pagemodel.objects.get(name=request.POST['name'], password=request.POST['password'])
            print("name=", Userdetails)
            request.session['name'] = Userdetails.name
            request.seesion.set_expiry(20)
            return HttpResponse('Login Successful', 'page1.html')
        except pagemodel.DoesNotExist as e:
            return HttpResponse('name/password Invalid..!')
    return render(request, 'log.html')


def time(request):  # this fun is for track the login session

    if 'name' in request.session:
        ver = request.session['name']
        return HttpResponse('login success')
    else:
        return HttpResponse('session expiry')


def studentlogin(request):
    if request.method == "POST":
        try:
            Userdetails = student.objects.get(student_name=request.POST['student_name'], password=request.POST['password'])
            print("firstname=", Userdetails)
            request.session['student_name'] = Userdetails.student_name
            request.session.set_expiry(40)
            return HttpResponse('Login Successful', 'student.html')
        except student.DoesNotExist as e:
            return HttpResponse('student name/password Invalid..!')
    return render(request, 'studentlogin.html')

def stutime(request):  # this fun is for track the login session

    if 'student_name' in request.session:
        ver = request.session['student_name']
        return HttpResponse('login success')
    else:
        return HttpResponse('session expiry')

def employeelogin(request):
    if request.method == "POST":
        try:
            Userdetails = employee.objects.get(emp_name=request.POST['emp_name'], password=request.POST['password'])
            print("emp_name=", Userdetails)
            request.session['emp_name'] = Userdetails.emp_name
            request.session.set_expiry(60)
            return HttpResponse('Login Successful', 'employee.html')
        except employee.DoesNotExist as e:
            return HttpResponse('employee name/password Invalid..!')
    return render(request, 'employeelogin.html')


def emptime(request):  # this fun is for track the login session

    if 'emp_name' in request.session:
        ver = request.session['emp_name']
        return HttpResponse('login success')
    else:
        return HttpResponse('session expiry')