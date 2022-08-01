from rest_framework import serializers
from .models import table

class currencyserializer(serializers.ModelSerializer):
    class Meta:
        model = table
        fields = 'currency',

class returnserializer(serializers.ModelSerializer):
    class Meta:
        model = table
        fields = '__all__'
