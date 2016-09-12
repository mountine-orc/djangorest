from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^importrates/$', views.importrates, name='importrates'),
    url(r'^apicurency/$', views.RateList.as_view()),
    url(r'^apicurencychanges/$', views.RateChanges.as_view()),
]