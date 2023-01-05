from rest_framework import serializers
import math
from .models import Decimalmodel

def fun(n,d):
    result = (f'%.{d}f' % n)
    return result

class decimalserializer(serializers.ModelSerializer):
    class Meta:
        model = Decimalmodel
        fields = 'number','digits'

    def create(self, validated_data):
        number = validated_data['number']
        digits = validated_data['digits']
        decimal_value = fun(n=number,d=digits)
        user = Decimalmodel.objects.create(number=validated_data['number'],digits=validated_data['digits'],
                                        decimal_value=decimal_value)
        user.save()
        return user

class retrieveserializer(serializers.ModelSerializer):
    class Meta:
        model = Decimalmodel
        fields = '__all__'