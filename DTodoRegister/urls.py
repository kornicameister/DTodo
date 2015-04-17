from django.conf.urls import include, url, patterns
from django.views.generic import TemplateView
from registration.backends.default.views import ActivationView

from DTodoRegister.views import DTRegisterView


_patterns = [
    url(r'^activate/complete/$', TemplateView.as_view(
        template_name='registration/activation_complete.html'),
        name='registration_activation_complete'),
    url(r'^activate/(?P<activation_key>\w+)/$',
        ActivationView.as_view(),
        name='registration_activate'),
    url(r'^register/$', DTRegisterView.as_view(),
        name='registration_register'),
    url(r'^register/complete/$', TemplateView.as_view(
        template_name='registration/registration_complete.html'),
        name='registration_complete'),
    url(r'^register/closed/$', TemplateView.as_view(
        template_name='registration/registration_closed.html'),
        name='registration_disallowed'),
    (r'', include('registration.auth_urls'))
]

urlpatterns = patterns('', *_patterns)