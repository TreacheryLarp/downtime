from django.conf.urls import patterns, url

from gamemaster import views

urlpatterns = patterns('',
    url(r'^closewindow$', views.close, name='closewindow'),
    url(r'^$', views.SessionListView.as_view(), name='sessions'),
    url(r'^s/(?P<session>\d+)/a$', views.ActionListView.as_view(), name='actions'),
    url(r'^s/(?P<session>\d+)/f$', views.ActionListView.as_view(), name='feedings'),
    url(r'^s/(?P<session>\d+)/d$', views.ActionListView.as_view(), name='disciplines'),
    url(r'^s/(?P<session>\d+)/c$', views.ActionListView.as_view(), name='characters'),
    url(r'^a/(?P<pk>\d+)$', views.ActionUpdate.as_view(), name='action'),
)
