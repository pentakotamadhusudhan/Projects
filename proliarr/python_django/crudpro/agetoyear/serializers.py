from rest_framework import serializers
from .models import *


import datetime
from datetime import date


def index(age):
    today = date.today()
    y = today.year - int(age)
    dob = f'{y}-{today.month}-{today.day}'
    da = datetime.datetime.now().strptime(dob,"%Y-%m-%d" ).date()
    print(type(da))
    print(da)
    return da



class converterserializer(serializers.ModelSerializer):
    class Meta:
        model = reversage
        fields = ['firstname', 'lastname', 'age']

    def create(self, validated_data):
        age = validated_data['age']
        print(type(age))
        convert = index(age)
        print(convert)
        user = reversage.objects.create(firstname=validated_data['firstname'],
                                        lastname=validated_data['lastname'],
                                        age=validated_data['age'], dob=convert)
        user.save()
        return user


class dataserializer(serializers.ModelSerializer):
    class Meta:
        model = reversage
        fields = ['firstname', 'lastname', 'age', 'dob']
