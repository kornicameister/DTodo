from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from DTodo.forms.forms import TodoItemForm
from DTodo.models import Todo
from DTodo.models import TodoItem
from DTodo.models import TodoList
from DTodo.models import Tag



# Register your models here.
admin.site.register(Tag)


class _AuditableAdminModel(admin.ModelAdmin):
    date_hierarchy = 'updated_at'
    exclude = [
        'created_at',
        'updated_at',
        'created_by',
        'updated_by'
    ]


class _TodoItemInline(admin.TabularInline):
    model = TodoItem
    form = TodoItemForm
    extra = 0

    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        if obj and obj.id:
            fields += ['done']
        return fields


@admin.register(Todo)
class TodoAdmin(_AuditableAdminModel):
    list_filter = ['visibility', 'completed', 'owned_by']
    actions = ['complete', 'un_complete']
    inlines = [_TodoItemInline]

    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        if obj and obj.id:
            fields += ['completed']
        return fields

    def complete(self, request, queryset):
        completed = []
        for todo in queryset:
            if todo.can_complete():
                todo.completed = True
                completed.append(todo.id)

        if len(completed) > 0:
            queryset.filter(id__in=completed).update(completed=True)

            completed = '%s todos were' % len(completed)
            self.message_user(request,
                              "%s successfully marked as completed." %
                              completed)

    def un_complete(self, request, queryset):
        completed = []
        for todo in queryset:
            if todo.completed:
                todo.completed = False
                completed.append(todo.id)

        if len(completed) > 0:
            queryset.filter(id__in=completed).update(completed=False)

            completed = '%s todos were' % len(completed)
            self.message_user(request,
                              "%s successfully marked as not completed." %
                              completed)

    complete.short_description = _('Mark item as completed')
    un_complete.short_description = _('Mark item as not completed')


@admin.register(TodoItem)
class TodoItemAdmin(_AuditableAdminModel):
    list_filter = ['todo__name', 'done']


@admin.register(TodoList)
class TodoListAdmin(_AuditableAdminModel):
    pass