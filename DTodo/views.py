from django.shortcuts import render

from DTodo.common import utils


def index_view(request):
    return render(
        request=request,
        template_name='index/index.html',
        context={
            'title': utils.get_view_title('Index')
        }
    )


