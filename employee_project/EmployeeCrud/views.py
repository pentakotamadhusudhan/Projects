from django.shortcuts import render

from .Crud.Employee_get_all import Employee_get
from .Crud.Employee_registration import employeeRegistration
# from .Employee_registration import *
# Create your views here.
employeeRegistration()
Employee_get()