from rest_framework import serializers
from .models import *

from datetime import datetime
from dateutil.relativedelta import relativedelta


def diffdate(a1, a2):
    d1 = datetime.strptime(a1, '%Y-%m-%d')
    d2 = datetime.strptime(a2, '%Y-%m-%d')
    time_difference = relativedelta(d2, d1)
    difference_in_years = f'{time_difference.years}years {time_difference.months}months {time_difference.days}days'
    return difference_in_years


class converterserializer(serializers.ModelSerializer):
    class Meta:
        model = agetable
        fields = ['date1', 'date2']

    def create(self, validated_data):
        date1 = str(validated_data['date1'])
        date2 = str(validated_data['date2'])
        convert = diffdate(date1, date2)
        user = agetable.objects.create(date1=date1,
                                       date2=date2, diff=convert)
        user.save()
        return user


class dataserializer(serializers.ModelSerializer):
    class Meta:
        model = agetable
        fields = ['date1', 'date2', 'diff']
