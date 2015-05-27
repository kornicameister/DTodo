from django.conf.urls import url
from django.views.decorators.cache import cache_page

from DTodo.view.todoList.todo_list import TodoListListView, TodoListDetailView, \
    TodoListCreateView, TodoListDeleteView, TodoListEditView

urlpatterns = [
    url(regex=r'^/all$',
        view=TodoListListView.as_view(),
        name='all'),
    url(regex=r'^/(?P<pk>\d+)(/(?P<slug>[-\w]+))?$',
        view=cache_page(60 * 15)(TodoListDetailView.as_view()),
        name='view'),
    url(regex=r'^/new',
        view=TodoListCreateView.as_view(),
        name='create'),
    url(regex=r'^/delete/(?P<pk>\d+)',
        view=TodoListDeleteView.as_view(),
        name='delete'),
    url(regex=r'^/edit/(?P<pk>\d+)',
        view=TodoListEditView.as_view(),
        name='edit'),
]
