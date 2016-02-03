from django.conf.urls import patterns, include, url
from django.contrib import admin

from players.forms import LoginForm

urlpatterns = patterns('',
    url(r'^logout/$','django.contrib.auth.views.logout',
        {'next_page': '/'}),

    url('^', include('django.contrib.auth.urls')),

    url(r'^gm/', include('gamemaster.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^', include('players.urls')),
)
