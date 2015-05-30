from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, CreateView, DeleteView, UpdateView
from sortable_listview import SortableListView
from django.utils.translation import ugettext_lazy as _

from DTodo.contants import PAGING_OPTS
from DTodo.forms.forms import TodoListForm
from DTodo.models import TodoList


class TodoListEditView(UpdateView):
    model = TodoList
    template_name = 'todoList/edit.html'
    success_url = reverse_lazy('dtodo:todoList:all')
    form_class = TodoListForm

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'buttons': {
                'submit': _('btn.ok'),
                'reset': _('btn.reset'),
                'cancel': _('btn.cancel')
            }
        })
        return context


class TodoListDeleteView(DeleteView):
    model = TodoList
    template_name = 'todoList/delete.html'
    success_url = reverse_lazy('dtodo:todoList:all')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            url = self.get_success_url()
            return HttpResponseRedirect(url)
        else:
            return super().post(request, *args, **kwargs)

    def get_success_url(self):
        if 'cancel' in self.request.POST:
            return self.success_url.format()
        return super().get_success_url()


class TodoListCreateView(CreateView):
    model = TodoList
    context_object_name = 'todoList'
    template_name = 'todoList/create.html'
    success_url = reverse_lazy('dtodo:todoList:all')
    form_class = TodoListForm

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'buttons': {
                'submit': _('btn.ok'),
                'reset': _('btn.reset'),
                'cancel': _('btn.cancel')
            }
        })
        return context

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            url = self.get_success_url()
            return HttpResponseRedirect(url)
        else:
            return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.owned_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        if 'cancel' in self.request.POST:
            return self.success_url.format()
        return super().get_success_url()


class TodoListDetailView(DetailView):
    model = TodoList
    context_object_name = 'todoList'
    template_name = 'todoList/detail.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class TodoListListView(SortableListView):
    model = TodoList
    template_name = 'todoList/all.html'
    context_object_name = 'todoList'
    paginate_by = PAGING_OPTS['SIZE']
    allowed_sort_fields = {
        'name': {
            'default_direction': '',
            'verbose_name': _('model.todo-list.name')
        },
        'visibility': {
            'default_direction': '-',
            'verbose_name': _('model.todo-list.visibility')
        }
    }
    default_sort_field = 'visibility'
    ordering = ['name', 'updated_at']

    def get_context_data(self, **kwargs):
        context = super(TodoListListView, self).get_context_data(**kwargs)
        context.update({
            'filter_by': TodoList.VISIBILITY
        })
        return context

    def get_queryset(self):
        user = self.request.user

        if user.is_authenticated():
            if not user.is_superuser:
                qs = TodoList.objects.filter(owned_by_id=user.id)
            else:
                qs = TodoList.objects.all()
        else:
            qs = TodoList.objects.filter(
                visibility=TodoList.PUBLIC_VISIBILITY
            )

        if 'filterBy' in self.request.GET:
            filter_by = self.request.GET.get('filterBy')
            qs = qs.filter(visibility=filter_by)

        qs = qs.order_by(*self.ordering)
        return qs.order_by(self.sort)
