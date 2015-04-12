from django.shortcuts import render
from django.views.decorators import cache


@cache.never_cache
def index(request):
    return render(
        request=request,
        template_name='index/index.html'
    )