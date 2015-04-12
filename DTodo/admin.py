from django.contrib import admin
from DTodo.models import Todo
from DTodo.models import TodoItem

# Register your models here.

admin.site.register(Todo)
admin.site.register(TodoItem)
