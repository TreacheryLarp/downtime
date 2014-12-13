from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required, permission_required
from django.forms.models import modelformset_factory

from downtime import views
from downtime import forms
from downtime import models

urlpatterns = patterns('',
    url(r'^$', views.profile, name='profile'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^s/(?P<pk>\d+)/$', views.session, name='session'),

    url(r'^s/submit/(?P<pk>\d+)$',
        login_required(views.SubmitWizard.as_view(
        [forms.DisciplineActivationForm, forms.FeedingForm,
        modelformset_factory(models.Action, formset=forms.ActionFormSet, fields=('action_type', 'description'))])),
        name='wizard'),
)
