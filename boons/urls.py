from django.conf.urls import patterns, url

from boons import views

urlpatterns = patterns('',
    url(r'^t/(?P<boon_key>\w+)$', views.transaction, name='transaction'),
    url(r'^p/(?P<boon_key>\w+)$', views.print_boon, name='print_boon'),
    url(r'^v/(?P<boon_key>\w+)$', views.view_boon, name='view_boon'),
)
