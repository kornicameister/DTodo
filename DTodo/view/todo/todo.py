from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.views.generic import DetailView, CreateView, UpdateView, \
    DeleteView
from sortable_listview import SortableListView

from DTodo.models import Todo
from DTodo.contants import PAGING_OPTS


class TodoListView(SortableListView):
    model = Todo
    template_name = 'todo/todo-list-view.html'
    context_object_name = 'todo'
    paginate_by = PAGING_OPTS['SIZE']
    allowed_sort_fields = {
        'name': {
            'default_direction': '',
            'verbose_name': _('model.todo.name')
        },
        'completed': {
            'default_direction': '-',
            'verbose_name': _('model.todo.completed')
        },
        'progress': {
            'default_direction': '-',
            'verbose_name': _('model.todo.progress')
        }
    }
    default_sort_field = 'completed'

    def get_context_data(self, **kwargs):
        context = super(TodoListView, self).get_context_data(**kwargs)
        context.update({
            'search_query': None,
            'filter_by': Todo.VISIBILITY
        })
        return context

    def get_queryset(self):
        if self.sort_field and self.sort_field == 'progress':
            sort_order = self.sort_order
            res = super(SortableListView, self).get_queryset()
            return sorted(res,
                          key=lambda todo: todo.progress,
                          reverse=(False if sort_order == '-' else True))

        return super().get_queryset()

    def get_ordering(self):
        ordering = Todo.Meta.ordering
        if not ordering:
            ordering = []

        return ['name'] + ordering


class TodoDetailView(DetailView):
    model = Todo
    template_name = 'todo/todo-detail-view.html'


class TodoCreateView(CreateView):
    model = Todo
    template_name = 'todo/todo-create-view.html'


class TodoEditView(UpdateView):
    model = Todo
    template_name = 'todo/todo-edit-view.html'


class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy('todo')
    template_name = 'todo/todo-delete-view.html'
