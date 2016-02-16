from django.conf.urls import patterns, url

from gamemaster import views
from django.contrib.admin.views.decorators import staff_member_required

urlpatterns = [
    url(r'^closewindow$', views.close, name='closewindow'),
    url(r'^$', staff_member_required(views.SessionListView.as_view()), name='sessions'),
    url(r'^s/(?P<session>\d+)/toggle$', staff_member_required(views.toggle_session), name='toggle_session'),
    url(r'^s/(?P<session>\d+)/a$', staff_member_required(views.ActionListView.as_view()), name='actions'),
    url(r'^s/(?P<session>\d+)/f$', staff_member_required(views.FeedingListView.as_view()), name='feedings'),
    url(r'^s/(?P<session>\d+)/d$', staff_member_required(views.DisciplineListView.as_view()), name='disciplines'),
    url(r'^s/(?P<session>\d+)/cs$', staff_member_required(views.CharacterListView.as_view()), name='characters'),
    url(r'^a/(?P<pk>\d+)$', staff_member_required(views.ActionUpdate.as_view()), name='action'),
    url(r'^f/(?P<pk>\d+)$', staff_member_required(views.FeedingUpdate.as_view()), name='feeding'),
    url(r'^c/(?P<pk>\d+)$', staff_member_required(views.CharUpdate.as_view()), name='character'),
]
