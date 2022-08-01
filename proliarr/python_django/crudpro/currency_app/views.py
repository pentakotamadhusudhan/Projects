from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response

from .serializers import currencyserializer,returnserializer
# Create your views here.
from num2words import num2words
from datetime import datetime
from .models import table
from rest_framework import generics


class CurrencyView(generics.GenericAPIView):
    serializer_class = currencyserializer

    def post(self, request):
        Currency = request.data.get('currency')
        conversion = num2words(Currency)
        ob = table()
        ob.currency = Currency
        ob.currency_word = conversion
        ob.save()

        return Response(returnserializer(ob).data)


#class RetriveView(generics.ListAPIView):
 #   queryset = currency_table.objects.all()
  #  serializer_class = currencyserializer