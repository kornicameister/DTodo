from registration.backends.default.views import RegistrationView
from registration.forms import RegistrationFormUniqueEmail


class DTRegisterView(RegistrationView):
    form_class = RegistrationFormUniqueEmail

    def get_success_url(self, request, user):
        return 'accounts:registration_complete', (), {}