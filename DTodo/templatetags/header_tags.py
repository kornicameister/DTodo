from django import template

from DTodo.models import Todo


register = template.Library()


@register.inclusion_tag(file_name='base/components/recent_todos.html',
                        name='recenttodos')
def most_completed_todos_tag(user, limit=10):
    is_authenticated = user.is_authenticated()
    order = '-updated_at'

    if not is_authenticated:
        qs = Todo.objects.filter(visibility=Todo.public_visibility())
    else:
        qs = Todo.objects.filter(owned_by_id=user)

    return {
        'todos': qs.order_by(order)[:limit]
    }


@register.inclusion_tag(
    file_name='base/components/most_completed_todos.html',
    name='mostcompletedtodos')
def most_completed_todos_tag(user, limit=10):
    is_authenticated = user.is_authenticated()
    order = '-updated_at'

    if not is_authenticated:
        qs = Todo.objects.filter(visibility=Todo.public_visibility())
    else:
        qs = Todo.objects.filter(owned_by_id=user)

    qs = qs.order_by(order)
    qs = sorted(qs, key=lambda todo: todo.progress, reverse=True)
    return {
        'todos': qs[:limit]
    }


@register.inclusion_tag(
    file_name='base/components/header-user.html',
    name='user_menu')
def user_menu_tag(user):
    is_authenticated = user.is_authenticated()
    return {
        'username': None if not is_authenticated else user.username,
        'authenticated': is_authenticated
    }