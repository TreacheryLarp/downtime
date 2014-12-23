from django.conf.urls import patterns, include, url
from django.contrib import admin

from players.forms import LoginForm

urlpatterns = patterns('',
    url(r'^', include('players.urls')),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'players/login.html', 'authentication_form': LoginForm}),
    url(r'^admin/', include(admin.site.urls)),
)
