from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.views.generic import CreateView
from sortable_listview import SortableListView

from DTodo.contants import PAGING_OPTS
from DTodo.models import Tag


class TagCreateView(CreateView):
    model = Tag
    fields = ['word', 'details']
    template_name = 'tag/tag-create-view.html'
    success_url = reverse_lazy('dtodo:tag:all')

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


class TagListView(SortableListView):
    model = Tag
    template_name = 'tag/tag-list-view.html'
    context_object_name = 'tags'
    paginate_by = PAGING_OPTS['SIZE']
    ordering = 'word'
    allowed_sort_fields = {
        'word': {
            'default_direction': '',
            'verbose_name': _('model.Tag.word')
        }
    }
    default_sort_field = 'word'