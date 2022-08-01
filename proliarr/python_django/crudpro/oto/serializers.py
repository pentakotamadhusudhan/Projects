from rest_framework import serializers
from .models import *


class form1serializer(serializers.ModelSerializer):
    class Meta:
        model = main1
        fields = ['UserName', 'Password']


class form2serializer(serializers.ModelSerializer):
    class Meta:
        model = main2
        fields = ['name','first_name','second_name','DOB']

