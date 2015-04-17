from django import template
from django_tools.middlewares import ThreadLocal

from DTodo.models import Todo


register = template.Library()


@register.inclusion_tag(file_name='base/components/recent_todos.html',
                        name='recenttodos')
def recent_todos_tag(**kwargs):
    current_user = ThreadLocal.get_current_user()
    is_authenticated = current_user.is_authenticated()
    limit = kwargs.get('limit', 10)
    order = '-updated_at'

    if not is_authenticated:
        qs = Todo.objects.filter(visibility=Todo.public_visibility())
    else:
        qs = Todo.objects.filter(owned_by_id=current_user)

    return {
        'todos': qs.order_by(order)[:limit]
    }


@register.inclusion_tag(
    file_name='base/components/most_completed_todos.html',
    name='mostcompletedtodos')
def most_completed_todos_tag(**kwargs):
    current_user = ThreadLocal.get_current_user()
    is_authenticated = current_user.is_authenticated()
    order = '-updated_at'

    limit = kwargs.get('limit', 10)

    if not is_authenticated:
        qs = Todo.objects.filter(visibility=Todo.public_visibility())
    else:
        qs = Todo.objects.filter(owned_by_id=current_user)

    qs = qs.order_by(order)
    qs = sorted(qs, key=lambda todo: todo.progress, reverse=True)
    return {
        'todos': qs[:limit]
    }


@register.inclusion_tag(
    file_name='base/components/header-user.html',
    name='user_menu')
def user_menu_tag(user):
    # note that as example we pass user to the tag directly
    current_user = ThreadLocal.get_current_user()
    is_authenticated = current_user.is_authenticated()
    return {
        'username': None if not is_authenticated else current_user.username,
        'authenticated': is_authenticated
    }