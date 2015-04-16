from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.views.generic import DetailView, CreateView, UpdateView, \
    DeleteView
from sortable_listview import SortableListView

from DTodo.forms.forms import TodoForm
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
        # custom sort field, look at get_queryset
        'progress': {
            'default_direction': '-',
            'verbose_name': _('model.todo.progress')
        }
    }
    default_sort_field = 'completed'
    ordering = ['name', 'updated_at']

    def get_context_data(self, **kwargs):
        context = super(TodoListView, self).get_context_data(**kwargs)
        context.update({
            'search_query': None,
            'filter_by': Todo.VISIBILITY
        })
        return context

    def get_queryset(self):
        """
        Provides handler for progress sorting property
        As well as provides Todos only for currently logged
        user as specified by owned_by ref
        :return: query set
        """

        user = self.request.user
        qs = Todo.objects.filter(owned_by_id=user.id).order_by(*self.ordering)

        if self.sort_field and self.sort_field == 'progress':
            sort_order = self.sort_order
            return sorted(qs,
                          key=lambda todo: todo.progress,
                          reverse=(False if sort_order == '-' else True))

        return qs.order_by(self.sort)


class TodoDetailView(DetailView):
    model = Todo
    context_object_name = 'todo'
    template_name = 'todo/todo-detail-view.html'


class TodoCreateView(CreateView):
    model = Todo
    success_url = reverse_lazy('dtodo:todo:all')
    template_name = 'todo/todo-create-view.html'
    form_class = TodoForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'buttons': {
                'submit': _('btn.ok'),
                'reset': _('btn.reset'),
                'cancel': _('bt.cancel')
            }
        })
        return context


class TodoEditView(UpdateView):
    model = Todo
    success_url = reverse_lazy('dtodo:todo:all')
    template_name = 'todo/todo-edit-view.html'

class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy('dtodo:todo:all')
    template_name = 'todo/todo-delete-view.html'
