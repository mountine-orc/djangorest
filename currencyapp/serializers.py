from django.contrib.auth.models import User, Group
from currencyapp.models import Currency, Rate
from rest_framework import serializers


class RateSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(format="%Y-%m-%d", required=False, read_only=True)

    class Meta:
        model = Rate
        fields = ('date', 'value')

class CurrencySerializer(serializers.ModelSerializer):
    rates = RateSerializer(many=True, read_only=True)

    class Meta:
        model = Currency
        fields = ('code', 'rates')