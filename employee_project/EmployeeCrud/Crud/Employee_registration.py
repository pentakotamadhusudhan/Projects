from rest_framework import generics
from rest_framework.response import Response

from ..models import EmployeeModel
from ..serilizers import registration_serilizer

class employeeRegistration(generics.GenericAPIView):
    """
    You can create a EMployee
    Email is unique
    After fill the form
    You can get Employee ID like EMP000
    """
    serializer_class = registration_serilizer

    def post(self,request):
        try:
            email = request.data.get('Email')
            try:
                if EmployeeModel.objects.filter(Email=email):
                    print('madihbu')
                    return Response({
                        "Status":200,"message":"employe already exist","success":False
                    })

            except :
                ser = registration_serilizer(data=request.data)
                ser.is_valid()
                resp = ser.save()
                x=resp.id
                l = len(x)
                basicID = 'EMP000'
                emp_id = basicID[:-l] + x
                return Response({
                                "message":"employee created successfully",
                                "regid":"EMp002",
                                "success":True
                                })
        except AssertionError:
            print({"Status":400})
            return Response({"status":400,
                             "message":"invalid body request",
                             "sucess":False
                             })

