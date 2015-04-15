from django import forms

from DTodo.models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = (
            'name',
            'visibility',
            'tags',
            'list'
        )
