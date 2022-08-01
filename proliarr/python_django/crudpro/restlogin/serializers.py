from rest_framework import serializers
from .models import logintable


class loginserializer(serializers.ModelSerializer):
    class Meta:
        model = logintable
        fields = '__all__'




class passwordserializer(serializers.ModelSerializer):
    class Meta:
        model = logintable
        fields = 'username','password'
