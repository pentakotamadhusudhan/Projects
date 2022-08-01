from django.contrib.auth.models import User
from .models import resetmodel
from rest_framework import serializers


class regserializer(serializers.ModelSerializer):
    class Meta:
        model = resetmodel
        fields = 'username', 'email', 'password'


class resetserializer(serializers.ModelSerializer):
    class Meta:
        model = resetmodel
        fields = 'email', 'new_password', 're_type_password'


class loginserializer(serializers.ModelSerializer):
    class Meta:
        model = resetmodel
        fields = 'username', 'password'
