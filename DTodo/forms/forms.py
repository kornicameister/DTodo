from django import forms

from DTodo.models import Todo, Tag


class TodoForm(forms.Form):
    name = forms.CharField()
    visibility = forms.CharField(
        widget=forms.RadioSelect(
            choices=Todo.VISIBILITY
        ),
        initial=Todo.DEFAULT_VISIBILITY
    )
    tags = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(
            choices=Tag.objects.all()
        ),
        required=False
    )
    list = forms.ChoiceField(
        widget=forms.Select,
        required=False
    )