from django import template
from django.template.defaultfilters import stringfilter

import markdown

from players import models
from treachery import settings

register = template.Library()


@register.filter
@stringfilter
def markdownify(text):
    return markdown.markdown(text, safe_mode='escape')


@register.filter
def session_resolved_state_color(s):
    state = s['state']
    session = s['session']
    if session.is_open:
        return ''
    else:
        if state == models.RESOLVED:
            return 'list-group-item-success'
        elif state == models.UNRESOLVED:
            return 'list-group-item-info'
        elif state == models.PENDING:
            return 'list-group-item-warning'
        elif state == models.NO_ACTIONS:
            return ''


@register.filter
def session_resolved_state(s):
    state = s['state']
    session = s['session']
    if session.is_open:
        return '(Open)'
    else:
        if state == models.RESOLVED:
            return '(Resolved)'
        elif state == models.UNRESOLVED:
            return '(Waiting for GM)'
        elif state == models.PENDING:
            return '(Actions Pending!)'
        elif state == models.NO_ACTIONS:
            return '(Closed)'


@register.filter
def submission_resolved_state_color(submission, is_open):
    state = submission.resolved
    if is_open:
        return 'panel-default'
    else:
        if state == models.RESOLVED:
            return 'panel-success'
        elif state == models.UNRESOLVED:
            return 'panel-info'
        elif state == models.PENDING:
            return 'panel-warning'


@register.simple_tag
def app_version():
    return settings.APP_VERISON
