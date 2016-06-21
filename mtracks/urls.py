__author__ = 'Arvind'

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^tracks/$',views.tracks, name='tracks'),
    url(r'^genres/$',views.genres, name='genres'),
    url(r'^(?P<id>[0-9]+)/$', views.detail, name='detail'),
    #url(r'^(?P<genre_id>[0-9]+)/$', views.genre_detail, name='genre_detail'),

]
