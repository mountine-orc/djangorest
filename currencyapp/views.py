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

def index(request):
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #context = {'latest_question_list': latest_question_list}


    context = {}
    return render(request, 'currency/index.html', context)

def importrates(request, question_id):
    #pageresponse = urllib.request.urlopen('http://api.fixer.io/latest')
    #currencydata = json.loads(pageresponse.read().decode('utf-8'))
    #response = "You're looking at the results of question %s."
    #return HttpResponse(response % question_id)
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
    Chnges all curencies.
    """
    def get(self, request, format=None):
        rates = Currency.objects.exclude(code= u'EUR')
        for key in rates:
            pprint(key)
        serializer = CurrencySerializer(rates, many=True)
        return Response(serializer.data)