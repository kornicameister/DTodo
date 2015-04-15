from django.apps import AppConfig


class DTodoAppConfig(AppConfig):
    name = 'DTodo'
    label = 'DTodo'
    verbose_name = 'Django Todo'

    def ready(self):
        # noinspection PyUnresolvedReferences
        import DTodo.listeners
