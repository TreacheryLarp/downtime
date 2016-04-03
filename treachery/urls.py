from django.conf.urls import patterns, include, url
from django.contrib import admin, auth
import django.contrib.auth.views

from players.forms import LoginForm

urlpatterns = [
    url(r'^', include('players.urls')),
    url(r'^gm/', include('gamemaster.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^login', django.contrib.auth.views.login,
        {'authentication_form': LoginForm}),
    url(r'^', include('django.contrib.auth.urls')),
]
