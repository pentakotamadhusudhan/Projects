# import latest
from rest_framework import serializers
from .models import *
from .Crud.base64_convertion import *

class projectSerilizer(serializers.ModelSerializer):
    class Meta:
        model = projectModel
        fields = ['empId','title',"description"]

class qualificationserializer(serializers.ModelSerializer):
    class Meta:
        model = qualificationModel
        fields = ['qualificationName','fromDate','toDate','percentage','empId']

class registration_serilizer(serializers.ModelSerializer):
    image =

    class Meta:
        model = employeeModel
        fields = ['Name','Email','Age','Gender','PhoneNo','AddressDetails','HouseNo','Street','City','State','Photo']
    def create(self,validated_data):
        imgg = validated_data['Photo']

        bImage = base64Con(imgg)
        # print(bImage)
        try:
            if employeeModel.objects.latest('regId'):
                v=employeeModel.objects.latest('regId')
                print(v)
                empid = str('{:03}'.format(int(v.EmpId[-3:])+1))
                print(empid)
                print(type(empid))
                x =(f"EMP"+empid)
        except:
            x = 'EMP001'
        print('madijknas')
        user = employeeModel.objects.create(regId = x,
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
                                            Photo = bImage,)
        print(user)
        return user





class workserializer(serializers.ModelSerializer):
    class Meta:
        model = work_Experience
        fields = ['workExperience','companyName','fromDate','toDate','companyAddress','empId']


class get_serializer(serializers.ModelSerializer):
    qualifications = qualificationserializer(read_only=True,many=True)
    project = projectSerilizer(read_only=True,many=True)
    workExperience = workserializer(read_only=True,many=True)
    class Meta:
        model = employeeModel
        fields = ['Name','Email','Age','Gender','PhoneNo','AddressDetails','HouseNo','Street','City','State','workExperience','Photo','qualifications','project']

    depth = 1



class Updateserializer(serializers.ModelSerializer):
    qualifications = qualificationserializer(read_only=True, many=True)
    project = projectSerilizer(read_only=True, many=True)
    workExperience = workserializer(read_only=True, many=True)
    class Meta:
        model = employeeModel
        fields = ['Name','Email','Age','Gender','PhoneNo','AddressDetails','HouseNo','Street','City','State','workExperience','Photo','qualifications','project']


class deleteserialzer(serializers.SerializerMetaclass):
    Empid= serializers.CharField(max_length=10)

    class Meta:
        model = employeeModel
        fields = ['EmpId']



