from currencyapp.models import Currency, Rate
from currencyapp.serializers import RateSerializer, CurrencySerializer
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from datetime import datetime, timedelta
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import urllib, json
import pprint
import collections

def index(request):
    context = {}
    return render(request, 'currency/index.html', context)


def rateChanges(request):
    context = {}
    return render(request, 'currency/rateChange.html', context)

def importrates(request):
    availablecurencies = Currency.objects.values_list('code', flat=True)

    for count in range(1,11):
        date = (datetime.today() - timedelta(days=count)).date()
        datestring = date.strftime('%Y-%m-%d')
        pageresponse = urllib.request.urlopen('http://api.fixer.io/' + datestring)
        currencydata = json.loads(pageresponse.read().decode('utf-8'))
        
        for key, value in currencydata["rates"].items():
            if key in availablecurencies:
                currency = Currency.objects.get(code=key)
                pprint.pprint(currency)
                q = Rate(value=value, date=date, currency=currency)
                pprint.pprint(q)
                q.save()

    return HttpResponse("Currencies is exported")

class RateList(APIView):
    """
    List all curencies.
    """
    def get(self, request, format=None):
        rates = Currency.objects.exclude(code= u'EUR')
        serializer = CurrencySerializer(rates, many=True)
        return Response(serializer.data)


class RateChanges(APIView):
    """
    Return dynamic of changes curencies
    """
    def get(self, request, format=None):
        currencies = Currency.objects.exclude(code= u'EUR')

        legend = ["Year"];
        rateDict = collections.OrderedDict();

        for currency in currencies:
            rates = currency.rates.order_by('date')
            startPeriodValue = 0
            code = currency.code
            legend.append(code)
            
            for rate in rates:
                print(str(rate.date))
                if str(rate.date) not in rateDict:
                    rateDict[str(rate.date)] = [str(rate.date)]
                
                if startPeriodValue == 0:
                	startPeriodValue = rate.value
                rateDict[str(rate.date)].append(rate.value/startPeriodValue);
        
        rateList = list(rateDict.values())
        rateList.insert(0,legend)

        return Response(rateList)