from django.contrib import admin

from DTodo.models import Todo
from DTodo.models import TodoItem
from DTodo.models import TodoList
from DTodo.models import Tag


# Register your models here.

admin.site.register(Todo)
admin.site.register(TodoItem)
admin.site.register(TodoList)
admin.site.register(Tag)
