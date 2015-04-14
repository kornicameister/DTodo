from django.core.urlresolvers import reverse_lazy
from django.templatetags.future import url
from django.views.decorators.cache import cache_page
from django.views.generic import ListView, DetailView, CreateView, UpdateView, \
    DeleteView

from DTodo.models import Todo


class TodoListView(ListView):
    model = Todo

    def get_context_data(self, **kwargs):
        context = super(TodoListView, self).get_context_data(**kwargs)
        return context


class TodoDetailView(DetailView):
    model = Todo


class TodoCreateView(CreateView):
    model = Todo


class TodoEditView(UpdateView):
    model = Todo


class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy('todo')


class TodoViews(object):
    """ Combines all Todo views into single access method """

    @staticmethod
    def url_patterns():
        return [
            url(regex=r'^todo/$',
                view=TodoListView.as_view(),
                name="todo"),
            url(regex=r'^todo/(?P<id>\d+)',
                view=cache_page(60 * 15)(TodoDetailView.as_view()),
                name="todo:read"),
            url(regex=r'^todo/new',
                view=TodoCreateView,
                name="todo:create"),
            url(regex=r'^todo/edit/(?P<id>\d+)',
                view=TodoEditView,
                name="todo:edit"),
            url(regex=r'^todo/delete/(?P<id>\d+)',
                view=TodoDeleteView,
                name="todo:delete"),
        ]