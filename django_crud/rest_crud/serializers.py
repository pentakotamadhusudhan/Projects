from rest_framework import serializers
from .models import employee


class classSerializer(serializers.ModelSerializer):
    class Meta:
        model = employee
        fields = '__all__'


class loginSerializer(serializers.ModelSerializer):
    class Meta:
        model = employee
        fields = 'name', 'password'


