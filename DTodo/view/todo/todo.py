from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext_lazy as _
from django.views.generic import DetailView, CreateView, UpdateView, \
    DeleteView
from sortable_listview import SortableListView

from DTodo.forms.forms import TodoCreateItemFormSet, \
    TodoEditItemFormSet
from DTodo.models import Todo, TodoItem
from DTodo.contants import PAGING_OPTS


class TodoListView(SortableListView):
    model = Todo
    template_name = 'todo/todo-list-view.html'
    context_object_name = 'todo'
    paginate_by = PAGING_OPTS['SIZE']
    allowed_sort_fields = {
        'name': {
            'default_direction': '',
            'verbose_name': _('models.Todo.name')
        },
        'completed': {
            'default_direction': '-',
            'verbose_name': _('models.Todo.completed')
        },
        # custom sort field, look at get_queryset
        'progress': {
            'default_direction': '-',
            'verbose_name': _('models.Todo.progress')
        }
    }
    default_sort_field = 'completed'
    ordering = ['name', 'updated_at']

    def get_context_data(self, **kwargs):
        context = super(TodoListView, self).get_context_data(**kwargs)
        context.update({
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
        if user.is_authenticated():
            if not user.is_superuser:
                qs = Todo.objects.filter(owned_by_id=user.id)
            else:
                qs = Todo.objects.all()
        else:
            qs = Todo.objects.filter(
                visibility=Todo.public_visibility()
            )

        if 'filterBy' in self.request.GET:
            filter_by = self.request.GET.get('filterBy')
            qs = qs.filter(visibility=filter_by)

        qs = qs.order_by(*self.ordering)

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

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class TodoCreateView(CreateView):
    model = Todo
    success_url = reverse_lazy('dtodo:todo:all')
    template_name = 'todo/todo-create-view.html'
    fields = (
        'name',
        'visibility',
        'tags',
        'list'
    )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.object = None

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    @staticmethod
    def _get_todo_item_formset(*args):
        return TodoCreateItemFormSet(*args)

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        todoitem_form = self._get_todo_item_formset()
        return self.render_to_response(
            self.get_context_data(
                form=form,
                todoitem_form=todoitem_form
            )
        )

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        todoitem_form = self._get_todo_item_formset(self.request.POST)

        is_valid = form.is_valid() and todoitem_form.is_valid()

        ti_names = []
        if is_valid:
            forms = todoitem_form.forms
            for ti_form in forms:
                ti_name = ti_form.cleaned_data['title']
                if ti_name not in ti_names:
                    ti_names.append(ti_name)
                else:
                    ti_form.add_error(None, ValidationError(
                        '%s duplicates already defined item title' % ti_name))

            is_valid = (len(ti_names) == len(todoitem_form.forms))

        if is_valid:
            return self._form_valid(form, todoitem_form)
        else:
            return self._form_invalid(form, todoitem_form)

    def _form_valid(self, form, todoitem_form):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        self.object = form.save()
        todoitem_form.instance = self.object
        todoitem_form.save()
        return HttpResponseRedirect(self.get_success_url())

    def _form_invalid(self, form, todoitem_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(
                form=form,
                todoitem_form=todoitem_form
            )
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'buttons': {
                'submit': _('btn.ok'),
                'reset': _('btn.reset'),
                'cancel': _('btn.cancel')
            },
            'new_item': True
        })
        return context


class TodoEditView(UpdateView):
    model = Todo
    success_url = reverse_lazy('dtodo:todo:all')
    template_name = 'todo/todo-edit-view.html'
    fields = (
        'name',
        'visibility',
        'tags',
        'list'
    )

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

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        values = TodoItem.objects.filter(todo=self.object).order_by(
            'done').values()
        return self.render_to_response(
            self.get_context_data(
                form=form,
                formsets=TodoEditItemFormSet(
                    instance=self.object,
                    save_as_new=False
                )
            )
        )

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        formsets = TodoEditItemFormSet(self.request.POST, instance=self.object)

        is_valid = form.is_valid() and formsets.is_valid()

        ti_names = []
        if is_valid:
            forms = formsets.forms
            for ti_form in forms:
                ti_name = ti_form.cleaned_data['title']
                if ti_name not in ti_names:
                    ti_names.append(ti_name)
                else:
                    ti_form.add_error(None, ValidationError(
                        '%s duplicates already defined item title' % ti_name))

            is_valid = (len(ti_names) == len(formsets.forms))

        if is_valid:
            return self._form_valid(form, formsets)
        else:
            return self._form_invalid(form, formsets)

    def _form_valid(self, form, items):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        self.object = form.save()
        items.instance = self.object
        items.save()
        return HttpResponseRedirect(self.get_success_url())

    def _form_invalid(self, form, items):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(
                form=form,
                formsets=items
            )
        )


class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy('dtodo:todo:all')
    template_name = 'todo/todo-delete-view.html'

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
