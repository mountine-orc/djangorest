from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ShowMainPage.as_view(), name='index'),
]