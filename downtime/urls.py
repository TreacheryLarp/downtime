from django.conf.urls import patterns, url

from downtime import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.SessionView.as_view(), name='session'),
)
