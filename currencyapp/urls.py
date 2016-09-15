from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ShowCurrencies.as_view(), name='index'),
    url(r'^ratechanges/$', views.ShowRateChanges.as_view(), name='rateChanges'),
    url(r'^importrates/$', views.ImportRates.as_view(), name='importrates'),
    url(r'^api/curency/$', views.RateList.as_view()),
    url(r'^api/curencychanges/$', views.RateChanges.as_view()),
]