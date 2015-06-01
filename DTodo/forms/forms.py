from django import forms
from django.forms import Textarea, inlineformset_factory

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
        fields = ('title', 'description', 'importance', 'done',)
        widgets = {
            'description': Textarea(attrs={'cols': 40, 'rows': 2})
        }


TodoItemFormSet = inlineformset_factory(
    parent_model=Todo,
    model=TodoItem,
    form=TodoItemForm,
    extra=1,
    can_delete=True,
    can_order=True
)


class TodoListForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = (
            'name',
            'visibility'
        )
