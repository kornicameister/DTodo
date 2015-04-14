from django.conf.urls import url
from django.views.decorators.cache import never_cache

from . import views
from DTodo.view.todo import TodoViews


urlpatterns = [
                  url(regex=r'^$',
                      view=never_cache(views.index_view),
                      name='index'),
                  # _todo-list views
                  url(r'^todo-list/$', view=None, name="todo-list"),
                  url(r'^todo-list/(?P<id>\d+)', view=None,
                      name="todo-list:read"),
                  url(r'^todo-list/new', view=None, name="todo-list:create"),
                  url(r'^todo-list/edit/(?P<id>\d+)', view=None,
                      name="todo-list:edit"),
                  # _todo-list views


                  # _todo-group views
                  url(r'^todo-group/$', view=None, name="todos"),
                  url(r'^todo-group/(?P<id>\d+)', view=None,
                      name="todo-group:read"),
                  url(r'^todo-group/new', view=None, name="todo-group:create"),
                  url(r'^todo-group/edit/(?P<id>\d+)', view=None,
                      name="todo-group:edit"),
                  # _todo-group views
              ] + TodoViews.url_patterns()