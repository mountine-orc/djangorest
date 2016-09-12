from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>[0-9]+)/$', views.importrates, name='importrates'),
    url(r'^apicurency/$', views.RateList.as_view()),
    url(r'^apicurencychanges/$', views.RateChanges.as_view()),
]