__author__ = 'Arvind'

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<track_id>[0-9]+)/$', views.track_detail, name='detail'),
]
