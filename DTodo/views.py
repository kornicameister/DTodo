from django.views.generic import TemplateView
from DTodo.common import utils


class IndexView(TemplateView):
    template_name = 'index/index.html'

    def get_context_data(self, **kwargs):
        return {
            'title': utils.get_view_title('Index')
        }