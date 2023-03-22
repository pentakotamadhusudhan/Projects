from django.shortcuts import render

from .Crud.Employee_get_all import Employee_get
from .Crud.Employee_registration import *
from .Crud.Employee_update import *
from .Crud.Employee_delete import *
# Create your views here.
employeeRegistration()
Employee_get()
projectmodel_view()
workingview()
qualificationview()
Updateview()
workUpdateview()
Employee_delete()