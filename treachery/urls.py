from django.conf.urls import patterns, include, url
from django.contrib import admin

from players.forms import LoginForm

urlpatterns = patterns('',
    url(r'^', include('players.urls')),

    url(r'^gm/', include('gamemaster.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^comments/', include('django_comments.urls')),

    url(r'^login', 'django.contrib.auth.views.login',
        {'authentication_form': LoginForm}),
    url(r'^', include('django.contrib.auth.urls')),

)
