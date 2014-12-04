from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'treachery.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^downtime/', include('downtime.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
