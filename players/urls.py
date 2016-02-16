from django.conf.urls import patterns, url

from players import views

urlpatterns = patterns('',
    url(r'^$', views.profile, name='profile'),
    url(r'^logout', views.logout_view, name='logout'),
    url(r'^profile$', views.profile, name='profile'),
    url(r'^s/(?P<session>\d+)$', views.session, name='session'),
    url(r'^s/submit/(?P<session>\d+)$', views.wizard, name='wizard'),
)
