from rest_framework import generics
from rest_framework.response import Response

from ..models import EmployeeModel
from ..serilizers import registration_serilizer


class Employee_get(generics.ListAPIView):
    serializer_class = registration_serilizer
    queryset = EmployeeModel.objects.all()