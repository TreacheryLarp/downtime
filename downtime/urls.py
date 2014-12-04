from django.conf.urls import patterns, url

from downtime import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<session_id>\d+)/$', views.session, name='session'),
)
