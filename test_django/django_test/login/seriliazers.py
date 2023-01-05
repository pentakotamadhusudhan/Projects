from rest_framework import serializers


class loginseriliazer(serializers.Serializer):
    name = serializers.CharField(max_length=10)
    password = serializers.CharField(max_length=12)
