from djongo.database import DatabaseError
from rest_framework import generics
from rest_framework.response import Response

from ..models import employeeModel
from ..serilizers import *

class employeeRegistration(generics.GenericAPIView):
    """
    You can create a EMployee
    Email is unique
    After fill the form
    You can get Employee ID like EMP000
    **Note* : * provide image Url,not image path, because in models we have taken as CharFileld for Base64 and we are uploading image file
    """
    serializer_class = registration_serilizer

    def post(self,request):
        try:
            email = request.data.get('Email')
            try:
                employeeModel.objects.get(Email=email)
                return Response({"status":200,
                             'Result':{"message": "Employee Already Exist",
                              "sucess": False},
                             })
            except:
                ser = registration_serilizer(data=request.data)
                ser.is_valid()
                resp = ser.save()
                print(resp.regId)
                return Response({"status":200,
                             'Result':{"message": "Employee created successfully",
                                       "regId":resp.regId,
                                       "sucess": True},
                             })
        except AssertionError:
            print({"Status":400})
            return Response({"status":400,
                             'Result':{"message": "invalid body request",
                              "sucess": False},
                             })

        except:
            return Response({
                             "status":500,
                             'Result':{"message": "employee created failed",
                              "sucess": False},
                             })

class projectmodel_view(generics.GenericAPIView):
    serializer_class = projectSerilizer

    def post(self,request):
        try:
            regId = request.data.get('regId')
            ser = self.get_serializer(data=request.data)
            ser.is_valid()
            resp = ser.save()

            return Response({"status":200,
                             'Result':{"message": "Employee Project details created successfully",
                                       "regId":regId,
                                       "sucess": True},
                             })

        except AssertionError:
            print({"Status": 400})
            return Response({"status": 400,
                             "message": "invalid body request",
                             "sucess": False
                             })
        except:
            return Response({
                "status": 500,
                'Result': {"message": "employee created failed",
                           "sucess": False},
            })

class workingview(generics.GenericAPIView):
    serializer_class = workserializer

    def post(self,request):
        Empid = request.data.get('regId')
        try:
            ser = self.get_serializer(data=request.data)
            ser.is_valid()
            resp = ser.save()

            return Response({
                "Status":200,
                "Result":{"message": "employee created successfully",
                 "regid": Empid,
                 "success": True}
            })

        except AssertionError:
            print({"Status": 400})
            return Response({"status": 400,
                             "message": "invalid body request",
                             "sucess": False
                             })
        except:
            return Response({
                "status": 500,
                'Result': {"message": "employee created failed",
                           "sucess": False},
            })

class qualificationview(generics.GenericAPIView):
    serializer_class =  qualificationserializer

    def post(self,request):
        Empid = request.data.get('regId')
        try:
            ser = self.get_serializer(data=request.data)
            ser.is_valid()
            resp = ser.save()

            return Response({
                "Status":200,
                "Resuly":{"message": "employee created successfully",
                 "regid": Empid,
                 "success": True}
            })

        except AssertionError:
            print({"Status": 400})
            return Response({"status": 400,
                             "Reslut":{"message": "invalid body request",
                              "sucess": False}
                             })
        except:
            return Response({
                "status": 500,
                'Result': {"message": "employee created failed",
                           "sucess": False},
            })
