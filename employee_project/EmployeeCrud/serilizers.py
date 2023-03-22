from rest_framework import serializers
from .models import *


class projectSerilizer(serializers.ModelSerializer):
    class Meta:
        model = projectmodel
        fields = ['empId','Title',"description"]

class qualificationserializer(serializers.ModelSerializer):
    class Meta:
        model = qualificationmodel
        fields = ['qualificationName','fromDate','toDate','percentage','empId']

class registration_serilizer(serializers.ModelSerializer):
    # qualifications = qualificationserializer()
    # project = projectSerilizer()
    class Meta:
        model = EmployeeModel
        fields = ['Name','Email','Age','Gender','PhoneNo','AddressDetails','HouseNo','Street','City','State','Photo']
    def create(self,validated_data):
        # EmpId = f'EMP00+{str(id)}',
        x=EmployeeModel.objects.all()
        # print(EmployeeModel.objects.all().aggregate(latest=models.max('id'))['lastest'])



        user = EmployeeModel.objects.create(EmpId="EMP001",
                                            Name=validated_data['Name'],
                                            Email=validated_data['Email'],
                                            Age=validated_data['Age'],
                                            Gender = validated_data['Gender'],
                                            PhoneNo = validated_data['PhoneNo'],
                                            AddressDetails =validated_data['AddressDetails'],
                                            HouseNo = validated_data['HouseNo'],
                                            Street = validated_data['Street'],
                                            City = validated_data['City'],
                                            State = validated_data['State'],
                                            Photo = "xdcfvgbhnjmk",)
        return user





class workserializer(serializers.ModelSerializer):
    class Meta:
        model = Work_Experience
        fields = ['workExperience','CompanyName','FromDate','ToDate','CompanyAddress','empId']


class get_serializer(serializers.ModelSerializer):
    qualifications = qualificationserializer(read_only=True,many=True)
    project = projectSerilizer(read_only=True,many=True)
    workExperience = workserializer(read_only=True,many=True)
    class Meta:
        model = EmployeeModel
        fields = ['Name','Email','Age','Gender','PhoneNo','AddressDetails','HouseNo','Street','City','State','workExperience','Photo','qualifications','project']

    depth = 1



class Updateserializer(serializers.ModelSerializer):
    qualifications = qualificationserializer(read_only=True, many=True)
    project = projectSerilizer(read_only=True, many=True)
    workExperience = workserializer(read_only=True, many=True)
    class Meta:
        model = EmployeeModel
        fields = ['Name','Email','Age','Gender','PhoneNo','AddressDetails','HouseNo','Street','City','State','workExperience','Photo','qualifications','project']


class deleteserialzer(serializers.SerializerMetaclass):
    Empid= serializers.CharField(max_length=10)

    class Meta:
        model = EmployeeModel
        fields = ['EmpId']



