from rest_framework import serializers
from .models import *


class mainserializer(serializers.ModelSerializer):
    class Meta:
        model = main
        fields = 'name', 'surname'

class nextserializer(serializers.ModelSerializer):
    class Meta:
        model = nextform
        fields = '__all__'
