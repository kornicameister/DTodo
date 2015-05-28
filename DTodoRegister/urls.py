from django.conf.urls import patterns
from django.conf.urls import include
from django.conf.urls import url
from django.conf import settings
from django.views.generic.base import TemplateView

from registration.backends.default.views import ActivationView
from registration.backends.default.views import RegistrationView

_PREFIX = ''

urlpatterns = patterns(
    _PREFIX,
    url(regex=r'^activate/complete/$',
        view=TemplateView.as_view(
            template_name='registration/activation_complete.html'
        ),
        name='registration_activation_complete'),
    url(regex=r'^activate/(?P<activation_key>\w+)/$',
        view=ActivationView.as_view(),
        name='registration_activate'
        ),
    url(regex=r'^register/complete/$',
        view=TemplateView.as_view(
            template_name='registration/registration_complete.html'
        ),
        name='registration_complete'
        ),
    url(regex=r'^register/closed/$',
        view=TemplateView.as_view(
            template_name='registration/registration_closed.html'
        ),
        name='registration_disallowed'
        )
)

if getattr(settings, 'INCLUDE_REGISTER_URL', True):
    urlpatterns += patterns(_PREFIX,
                            url(regex=r'^register/$',
                                view=RegistrationView.as_view(),
                                name='registration_register'),
                            )

if getattr(settings, 'INCLUDE_AUTH_URLS', True):
    urlpatterns += patterns(_PREFIX, (r'', include('registration.auth_urls')))
