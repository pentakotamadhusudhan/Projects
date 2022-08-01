from rest_framework import serializers
from .models import saltmodel
import hashlib


class regserilizer(serializers.ModelSerializer):
    class Meta:
        model = saltmodel
        fields = 'name', 'email', 'password'

    def create(self, validated_data):
        name = validated_data['name']

        password = validated_data['password']
        email = validated_data['email']
        saltpassword = hashlib.md5(password.encode())
        ver = saltpassword.hexdigest()
        create_data = saltmodel.objects.create(name=name, password=password, update_password=ver, email=email)
        create_data.save()
        return create_data


class getserilizer(serializers.ModelSerializer):
    class Meta:
        model = saltmodel
        fields = 'name', 'email'


class logserilizer(serializers.ModelSerializer):
    class Meta:
        model = saltmodel
        fields = 'name', 'password'
