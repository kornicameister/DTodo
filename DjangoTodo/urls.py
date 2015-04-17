from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^dtodo/', include('DTodo.urls', namespace='dtodo')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('DTodoRegister.urls', namespace='accounts')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
