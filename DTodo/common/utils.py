__author__ = 'Tomasz'

from DTodo import contants


def get_view_title(title):
    if not title:
        raise RuntimeError('Title is not defined')

    return ('%s%s%s' % (
        contants.DEFAULT_PAGE_TITLE, contants.PAGE_TITLE_DELIM, title)).title()