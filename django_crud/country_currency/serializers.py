from rest_framework import serializers
from .models import Currency_symbol


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["country_currency"]
        model = Currency_symbol


class GetSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Currency_symbol