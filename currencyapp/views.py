from currencyapp.models import Currency, Rate
from currencyapp.serializers import CurrencySerializer
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime, timedelta
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
import urllib
import json
import collections
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class ShowCurrencies(View):
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'currency/index.html', context)


class ShowRateChanges(View):
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'currency/rateChange.html', context)


class ImportRates(View):
    """
    Import currency rates from api.fixer.io
    """
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        available_currencies = Currency.objects.values_list('code', flat=True)

        for count in range(1,11):
            date = (datetime.today() - timedelta(days=count)).date()
            date_string = date.strftime('%Y-%m-%d')
            page_response = urllib.request.urlopen('http://api.fixer.io/' + date_string)
            currency_data = json.loads(page_response.read().decode('utf-8'))

            for key, value in currency_data["rates"].items():
                if key in available_currencies:
                    currency = Currency.objects.get(code=key)
                    Rate.objects.update_or_create(date=date, currency=currency, defaults={'value': value})

        return HttpResponse("Currencies is imported")


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
        rate_dict = collections.OrderedDict();

        for currency in currencies:
            rates = currency.rates.order_by('date')
            start_period_value = 0
            code = currency.code
            legend.append(code)
            
            for i, rate in enumerate(rates):
                if str(rate.date) not in rate_dict:
                    rate_dict[str(rate.date)] = [str(rate.date)]
                
                if i == 0:
                    start_period_value = rate.value

                rate_dict[str(rate.date)].append(rate.value/start_period_value)
        
        rate_list = list(rate_dict.values())
        rate_list.insert(0, legend)

        return Response(rate_list)
