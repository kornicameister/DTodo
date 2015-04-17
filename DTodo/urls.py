from django.conf.urls import include, url
from django.views.decorators.cache import never_cache

from . import views


urlpatterns = [
    url(r'^$', view=never_cache(views.index_view), name='index'),
    url(r'^todo', include('DTodo.view.todo.urls', namespace='todo')),
    url(r'^tag', include('DTodo.view.tag.urls', namespace='tag')),
    url(r'^user', include('registration.auth_urls', namespace='user'))
]

# urlpatterns += [
# url(r'^todo-list/$', view=None, name="todo-list"),
# url(r'^todo-list/(?P<id>\d+)', view=None,
# name="todo-list:read"),
# url(r'^todo-list/new', view=None, name="todo-list:create"),
# url(r'^todo-list/edit/(?P<id>\d+)', view=None,
#         name="todo-list:edit"),
#     # _todo-list views
#
#
#     # _todo-group views
#     url(r'^todo-group/$', view=None, name="todos"),
#     url(r'^todo-group/(?P<id>\d+)', view=None,
#         name="todo-group:read"),
#     url(r'^todo-group/new', view=None, name="todo-group:create"),
#     url(r'^todo-group/edit/(?P<id>\d+)', view=None,
#         name="todo-group:edit"),
#     # _todo-group views
# ]