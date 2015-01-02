from django.conf.urls import patterns, url

from gamemaster import views

urlpatterns = patterns('',
    url(r'^$', views.SessionListView.as_view(), name='sessions'),
)
