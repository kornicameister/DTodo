from django import forms

from DTodo.models import Todo, TodoItem, TodoList


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = (
            'name',
            'visibility',
            'tags',
            'list'
        )


class TodoItemForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = (
            'title',
            'description',
            'importance'
        )


class TodoListForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = (
            'name',
            'visibility'
        )
