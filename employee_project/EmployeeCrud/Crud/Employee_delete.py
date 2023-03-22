from rest_framework import generics
from rest_framework.response import Response

from ..models import EmployeeModel
from ..serilizers import deleteserialzer

class Employee_delete(generics.GenericAPIView):
    serializer_class =deleteserialzer

    def delete(self,request,Empid):
        # empid = request.data.get('Empid')
        member = EmployeeModel.objects.get(EmpId=Empid)
        member.delete()
        return  Response({"status":200,
                          "Result":{"message": "employee deleted successfully",
                           "sucess": False}
                             })