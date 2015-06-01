from django.conf.urls import url

from DTodo.view.todo.todo import TodoListView, TodoDetailView, TodoCreateView, \
    TodoEditView, TodoDeleteView

urlpatterns = [
    url(regex=r'^/all$',
        view=TodoListView.as_view(),
        name='all'),
    url(regex=r'^/(?P<pk>\d+)(/(?P<slug>[-\w]+))?$',
        view=TodoDetailView.as_view(),
        name='view'),
    url(regex=r'^/new',
        view=TodoCreateView.as_view(),
        name='create'),
    url(regex=r'^/edit/(?P<pk>\d+)',
        view=TodoEditView.as_view(),
        name='edit'),
    url(regex=r'^/delete/(?P<pk>\d+)',
        view=TodoDeleteView.as_view(),
        name='delete'),
]
