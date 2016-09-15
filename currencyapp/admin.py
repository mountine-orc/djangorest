from django.contrib import admin

from .models import Currency, Rate, UserCurrency

admin.site.register(Currency)
admin.site.register(Rate)
admin.site.register(UserCurrency)
