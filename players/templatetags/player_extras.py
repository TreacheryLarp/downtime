from django import template
from django.template.defaultfilters import stringfilter
import markdown

register = template.Library()

@register.filter
@stringfilter
def markdownify(text):
    return markdown.markdown(text, safe_mode='escape')
