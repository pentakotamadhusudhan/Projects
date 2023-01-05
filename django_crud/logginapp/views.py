
import datetime
import logging

from django.http import HttpResponse
from django.shortcuts import render
from .models import loginmodel

logger = logging.getLogger('django')


def webpage(request):
    if request.method == "POST":
        dbdata = loginmodel()
        dbdata.firstname = request.POST.get('firstname')
        dbdata.lastname = request.POST.get('lastname')
        dbdata.password = request.POST.get('password')
        dbdata.save()
        return HttpResponse('register success')
    return render(request, 'reglog.html')


def login(request):
    if request.method == "POST":
        first_name = request.POST['firstname']
        pass_word = request.POST['password']
        try:
            dbdata = loginmodel.objects.get(firstname=first_name)
            if pass_word == dbdata.password:
                return HttpResponse("Login Successful")
            else:
                return HttpResponse("firstname/password is in valid")
        except:
            return HttpResponse(logger.info("Your Enter Details Incorrect " + str(datetime.datetime.now())))
    return render(request, 'loggin.html')