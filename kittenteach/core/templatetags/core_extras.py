import time

from django import template

register = template.Library()
timestamp = int(time.time())


@register.simple_tag
def timecache():
    return f'?v={timestamp}'
