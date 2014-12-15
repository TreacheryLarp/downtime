from django.conf.urls import patterns, url

from downtime import views

urlpatterns = patterns('',
    url(r'^$', views.profile, name='profile'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^s/(?P<session>\d+)/$', views.session, name='session'),
    url(r'^s/submit/(?P<session>\d+)$', views.wizard, name='wizard'),
)
