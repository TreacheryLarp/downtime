from django.conf.urls import patterns, include, url
from django.contrib import admin

from players.forms import LoginForm

urlpatterns = patterns('',
    url(r'^logout/$','django.contrib.auth.views.logout',
        {'next_page': '/'}),
    url(r'^password_change/$', 'django.contrib.auth.views.password_change'),
    url(r'^password_change_done/$',
        'django.contrib.auth.views.password_change_done',
        name='password_change_done'),
    url(r'^login/$', 'django.contrib.auth.views.login',
        {'authentication_form': LoginForm}),
    url(r'^gm/', include('gamemaster.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^', include('players.urls')),
)
