# your_app/templatetags/embed_filters.py

from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name='embed')
@stringfilter
def embed(value):
    # Your logic to convert the video URL to an embeddable format goes here
    # Example: return the value as is
    return value
