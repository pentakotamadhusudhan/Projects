from rest_framework import serializers
from .models import *
# from .dob import calculateage
from datetime import datetime
import datetime
from django.conf import settings

from datetime import date


def calculateage(birthDate):
    today = date.today()
    age = today.year - birthDate.year
    return age


class converterserializer(serializers.ModelSerializer):
    date_of_birth = input_formats = settings.DATE_INPUT_FORMATS

    class Meta:
        model = dobtable
        fields = ['dob']

    def create(self, validated_data):
        dob = validated_data['dob']
        dateofbirth = datetime.datetime.strptime(str(dob), '%Y-%m-%d').date()

        age = calculateage(dateofbirth)
        a = dobtable.objects.create(dob=validated_data['dob'], Age=age)
        a.save()
        return a


class dataserializer(serializers.ModelSerializer):
    class Meta:
        model = dobtable
        fields = ['dob', 'Age']
