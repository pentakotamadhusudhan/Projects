from rest_framework import generics
from rest_framework.response import Response

from ..models import employeeModel
from rest_framework import generics

from ..serilizers import *


class Updateview(generics.GenericAPIView):
    serializer_class = registration_serilizer

    def put(self,request,EmpId):
        emp = employeeModel.objects.get(regId=EmpId)
        ser = Updateserializer(instance=emp,data=request.data)
        ser.is_valid()
        ser.save()

        return Response({
            'Result':ser.data,
        })


class qualificationupdateview(generics.GenericAPIView):
    serializer_class = qualificationserializer

    def put(self,request,EmpId):
          try:
              try:
                    emp = qualificationModel.objects.get(empId=EmpId)
                    ser = qualificationserializer(instance=emp,data=request.data)
                    ser.is_valid()
                    ser.save()

                    return Response({
                        "Status": 200,
                        "Resuly": {"message": "employee created successfully",
                                   "regid": EmpId,
                                   "success": True}
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
                  'Result': {"message": "employee created failed",
                             "sucess": False},
              })


class projectupdateview(generics.GenericAPIView):
    serializer_class = projectSerilizer

    def put(self,request,EmpId):
        try:
            emp = projectModel.objects.get(empId=EmpId)
            ser = projectSerilizer(instance=emp,data=request.data)
            ser.is_valid()
            ser.save()

            return Response({
                "Status": 200,
                "Resuly": {"message": "employee created successfully",
                           "regid": EmpId,
                           "success": True}
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
                'Result': {"message": "employee created failed",
                           "sucess": False},
            })


class workUpdateview(generics.GenericAPIView):
    serializer_class = workserializer


    def put(self,request,EmpId):
        try:
            try:
                emp = work_Experience.objects.get(empId=EmpId)
                ser = workserializer(instance=emp,data=request.data)
                ser.is_valid()
                ser.save()

                return Response({
                    "Status": 200,
                    "Resuly": {"message": "employee created successfully",
                               "regid": EmpId,
                               "success": True}
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
                'Result': {"message": "employee created failed",
                           "sucess": False},
            })
