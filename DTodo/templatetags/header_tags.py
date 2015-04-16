from django import template
from django_tools.middlewares import ThreadLocal

from DTodo.models import Todo


register = template.Library()


@register.inclusion_tag(file_name='base/components/recent_todos.html',
                        name='recenttodos')
def recent_todos_tag(**kwargs):
    current_user = ThreadLocal.get_current_user()
    limit = int(kwargs.get('limit', 10))

    return {
        'todos': Todo.objects.filter(owned_by_id=current_user).order_by(
            '-updated_at')[:limit]
    }


@register.inclusion_tag(
    file_name='base/components/most_completed_todos.html',
    name='mostcompletedtodos')
def most_completed_todos_tag(**kwargs):
    current_user = ThreadLocal.get_current_user()
    limit = int(kwargs.get('limit', 10))

    qs = Todo.objects.filter(owned_by_id=current_user)
    qs = sorted(qs,
                key=lambda todo: todo.progress,
                reverse=True)
    return {
        'todos': qs[:limit]
    }