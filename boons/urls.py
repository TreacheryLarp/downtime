from django.conf.urls import patterns, url

from boons import views

urlpatterns = patterns('',
    url(r'^t/(?P<boon>\w+)$', views.transaction, name='transaction'),
)
