from rest_framework import generics
from rest_framework.response import Response

from ..models import employeeModel
from ..serilizers import deleteserialzer

class Employee_delete(generics.GenericAPIView):
    serializer_class =deleteserialzer

    def delete(self,request,regId):
        """ Delete  the Employee details including
        - Project
        - Qualification
        - Work Experience details
        """
        try:
            member = employeeModel.objects.get(regId=regId)
            member.delete()
            return  Response({"status":200,
                              "Result":{"message": "employee deleted successfully",
                               "sucess": False}
                                 })
        except AssertionError:
            print({"Status": 400})
            return Response({"status": 400,
                             "Reslut": {"message": "invalid body request",
                                        "sucess": False}
                             })

        except:
            return Response({
                "status": 500,
                'Result': {"message": "employee deleted failed",
                           "sucess": False},
            })