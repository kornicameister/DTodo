from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'^dtodo/', include('DTodo.urls', namespace='dtodo')),
    url(r'^admin/', include(admin.site.urls)),
]
