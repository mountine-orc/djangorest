from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ratechanges/$', views.rateChanges, name='rateChanges'),
    url(r'^importrates/$', views.importrates, name='importrates'),
    url(r'^api/curency/$', views.RateList.as_view()),
    url(r'^api/curencychanges/$', views.RateChanges.as_view()),
]