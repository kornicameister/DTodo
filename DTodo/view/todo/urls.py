from django.conf.urls import url
from django.views.decorators.cache import cache_page

from DTodo.view.todo.todo import TodoListView, TodoDetailView, TodoCreateView, \
    TodoEditView, TodoDeleteView


urlpatterns = [
    url(regex=r'^/all$',
        view=TodoListView.as_view(),
        name='all'),
    url(regex=r'^/(?P<pk>\d+)',
        view=cache_page(60 * 15)(TodoDetailView.as_view()),
        name='view'),
    url(regex=r'^/new',
        view=TodoCreateView.as_view(),
        name='create'),
    url(regex=r'^/edit/(?P<id>\d+)',
        view=TodoEditView.as_view(),
        name='edit'),
    url(regex=r'^/delete/(?P<id>\d+)',
        view=TodoDeleteView.as_view(),
        name='delete'),
]