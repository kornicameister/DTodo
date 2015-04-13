from django import template
from DTodo.contants import PAGE_TITLE_DELIM

register = template.Library()


@register.simple_tag(name="pageHeader")
def page_header(title, **kwargs):
    if not title:
        title = kwargs['default']

    if PAGE_TITLE_DELIM in title:
        title = title.split(sep=PAGE_TITLE_DELIM)
        title = title[1]

    return title.title()