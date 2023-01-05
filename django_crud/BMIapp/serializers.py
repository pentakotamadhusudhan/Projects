from rest_framework import serializers
from .models import bmimodel


class bmiserializer(serializers.ModelSerializer):
    class Meta:
        model = bmimodel
        fields = 'weight', 'height'


class showserializer(serializers.ModelSerializer):
    class Meta:
        model = bmimodel
        fields = '__all__'
