from django.conf.urls import patterns, include, url
from django.contrib import admin

from downtime.forms import LoginForm

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'treachery.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include('downtime.urls')),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'downtime/login.html', 'authentication_form': LoginForm}),
    url(r'^admin/', include(admin.site.urls)),
)
