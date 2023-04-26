from rest_framework import serializers
from .models import firstmodel

class firstser(serializers.ModelSerializer):
    class Meta:
        model = firstmodel
        fields = "__all__"