from django import template

from DTodo.contants import PAGE_TITLE_DELIM
from DTodo.models import Todo


register = template.Library()


@register.simple_tag(name="pageHeader")
def page_header(title, **kwargs):
    if not title:
        title = kwargs['default']

    if PAGE_TITLE_DELIM in title:
        title = title.split(sep=PAGE_TITLE_DELIM)
        title = title[1]

    return title.title()


@register.simple_tag
def todo_contextual_class_visibility(visiblity):
    if not visiblity:
        return ''
    elif visiblity == Todo.PUBLIC_VISIBILITY:
        return 'list-group-item-info'
    else:
        return 'list-group-item-warning'


@register.simple_tag
def percent_value(val):
    if not val:
        return 0.0
    return val * 100.0