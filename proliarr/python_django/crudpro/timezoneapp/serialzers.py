from rest_framework import serializers
from .models import *
import pytz
from pytz import country_timezones
import datetime


class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = timezonemodel
        fields = ['timezone','DateTime']

    def create(self, validated_data):
        timezone = validated_data['timezone']
        zone_time = datetime.datetime.now(pytz.timezone(timezone))
        print(zone_time)

        user =timezonemodel.objects.create(timezone=timezone, DateTime=zone_time)
        user.save()
        return user






