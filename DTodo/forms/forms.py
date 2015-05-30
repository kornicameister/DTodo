from django import forms
from django.forms import Textarea, inlineformset_factory, TextInput

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
        fields = ('title', 'description', 'importance')
        widgets = {
            'description': Textarea(attrs={'cols': 40, 'rows': 2})
        }


class TodoEditItemForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ('title', 'done',)
        widgets = {
            'title': TextInput(attrs={'readonly': 'readonly'})
        }


TodoCreateItemFormSet = inlineformset_factory(
    parent_model=Todo,
    model=TodoItem,
    form=TodoItemForm,
    extra=1,
    can_delete=True,
    can_order=True
)

TodoEditItemFormSet = inlineformset_factory(
    parent_model=Todo,
    model=TodoItem,
    form=TodoEditItemForm,
    extra=0,
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
