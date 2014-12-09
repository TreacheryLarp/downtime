from django.conf.urls import patterns, url

from downtime import views

urlpatterns = patterns('',
    url(r'^$', views.profile, name='profile'),
    url(r'^s/(?P<pk>\d+)/$', views.SessionView.as_view(), name='session'),
)
