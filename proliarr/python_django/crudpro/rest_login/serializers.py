from rest_framework import serializers
from .models import Employee


class classSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class loginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = 'name', 'password'


