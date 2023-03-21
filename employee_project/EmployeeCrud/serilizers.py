from rest_framework import serializers
from .models import *


class projectSerilizer(serializers.ModelSerializer):
    class Meta:
        model = projectmodel
        fields = ['Title',"description"]

class qualificationserializer(serializers.ModelSerializer):
    class Meta:
        model = qualificationmodel
        fields = ['qualificationName','fromDate','toDate','percentage']

class registration_serilizer(serializers.ModelSerializer):
    qualifications = qualificationserializer()
    project = projectSerilizer()
    class Meta:
        model = EmployeeModel
        fields = ['Name','Email','Age','Gender','PhoneNo','AddressDetails','HouseNo','Street','City','State','CompanyName','FromDate','ToDate','CompanyAddress','Precentage','Photo','qualifications','project']
    # def create(self, validated_data):

    #     user = EmployeeModel.objects(Name=validated_data['Name'],Email=validated_data['Email'],
    #                                  Age=validated_data['Age'],
    #                                  Gender = validated_data['Gender'],
    #                                  PhoneNo = validated_data['PhoneNo'],
    #                                  AddressDetails =validated_data['AddressDetails'],
    #                                  HouseNo = validated_data['HouseNo'],
    #                                  Street = validated_data['Street'],
    #                                  City = validated_data['City'],
    #                                  State = validated_data['State'],
    #                                  CompanyName = validated_data['CompanyName'],
    #                                  FromDate = validated_data['FromDate'],
    #                                  ToDate = validated_data['ToDate'],
    #                                  CompanyAddress = validated_data['CompanyAddress'],
    #                                  )
    #     return  user


