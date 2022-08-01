from django.shortcuts import render
from datetime import datetime
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .serializers import CurrencySerializer, GetSerializer
from .models import Currency_symbol
from countryinfo import CountryInfo
from currency_symbols import CurrencySymbols
from rest_framework.response import Response


def currency(name):
    name = CountryInfo(name)
    name1 = name.currencies()  # currencies is in-built function
    result = name1[0]   # 0 is index list if change the value(0) .it shows error "list index out of range"
    return result


def symbol(symbol):
    name3 = CurrencySymbols.get_symbol(symbol)
    return name3


class Reg(generics.GenericAPIView):
    serializer_class = CurrencySerializer

    def post(self, request, *args, **kwargs):
        date1 = datetime.now()
        cr_name = request.data.get('country_currency')
        country_cur = currency(cr_name)
        detail = symbol(country_cur)
        # print(detail)
        details = Currency_symbol()
        details.country = cr_name
        details.currency = country_cur
        details.currency_symbol = detail
        details.time = date1.strftime("%y-%m-%d")
        details.save()
        return Response(GetSerializer(details).data)