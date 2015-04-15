from DTodo.models import Todo

__author__ = "Tomasz"
__doc__ = 'Contains filters for models'

import django_filters as filters


class TodoVisiblityFilter(filters.FilterSet):
    visiblity = filters.ChoiceFilter(Todo.VISIBILITY)

    class Meta:
        model = Todo
        fields = ['visiblity']