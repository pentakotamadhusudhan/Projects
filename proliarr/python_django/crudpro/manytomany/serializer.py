from rest_framework import serializers
from .models import studentmodel,employeemodel,peoplemodel

class studentserializer(serializers.ModelSerializer):
    class Meta:
        model = studentmodel
        fields = '__all__'


class employeeserializer(serializers.ModelSerializer):
    class Meta:
        model = employeemodel
        fields = '__all__'

class peopleserializer(serializers.ModelSerializer):
    class Meta:
        model = peoplemodel
        fields = '__all__'