from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required, permission_required

from downtime import views
from downtime import forms

urlpatterns = patterns('',
    url(r'^$', views.profile, name='profile'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^s/(?P<pk>\d+)/$', views.session, name='session'),

    url(r'^s/(?P<pk>\d+)/submit/$',
        login_required(views.SubmitWizard.as_view(
        [forms.DisciplineActivationForm, forms.ActionForm])),
        name='wizard'),
)
