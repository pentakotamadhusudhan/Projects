from rest_framework import generics
from rest_framework.response import Response

from ..models import EmployeeModel
from ..serilizers import *


class Employee_get(generics.ListAPIView):
    serializer_class = get_serializer
    queryset = EmployeeModel.objects.all()