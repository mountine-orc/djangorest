from django.db import models
from django.contrib.auth.models import User


class Currency(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=3)

    def __str__(self):
        return self.name


class Rate(models.Model):
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='rates')
    date = models.DateField('date')
    value = models.FloatField(default=0.0)

    class Meta:
        unique_together = ('currency', 'date',)


class UserCurrency(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + ' - ' + self.currency.code
