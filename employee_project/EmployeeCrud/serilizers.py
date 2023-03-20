from rest_framework import serializers
from .models import EmployeeModel

class registration_serilizer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeModel
        fields = "__all__"
    # def create(self, validated_data):
    #     user = EmployeeModel.objects(validated_data['Name'],validated_data['Email'])
    #     return  user