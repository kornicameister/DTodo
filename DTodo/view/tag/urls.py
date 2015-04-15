from django.conf.urls import url

from DTodo.view.tag.tag import TagListView, TagCreateView


urlpatterns = [
    url(regex=r'^/all', view=TagListView.as_view(), name='all'),
    url(regex=r'^/new', view=TagCreateView.as_view(), name='create'),
]