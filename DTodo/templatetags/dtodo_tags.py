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
        return 'info'
    else:
        return 'warning'


@register.simple_tag
def percent_value(val):
    if not val:
        return 0.0
    return val * 100.0


@register.inclusion_tag(file_name='bootstrap_progress.html', name='progressbar')
def bootstrap_progress_bar(**kwargs):
    contextual_class = kwargs.get('contextual_class', 'progress-bar-info')
    min_value = float(kwargs.get('min_value', 0.0))
    max_value = float(kwargs.get('max_value', 100.0))
    value = float(kwargs.get('value', 0.0))

    if not value or value == 0.0:
        return 0.0

    value *= 100.0

    return {
        'min_value': min_value,
        'max_value': max_value,
        'contextual_class': contextual_class,
        'raw_value': value,
        'value': float("{0:.1f}".format(value))
    }