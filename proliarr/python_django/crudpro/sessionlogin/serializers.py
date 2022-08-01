from rest_framework import serializers
from rest_login.models import *
class loginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = 'name', 'password'
