from django.conf import settings
from django.db import models


class AuditableModel(models.Model):
    """
    AuditableModel subclass models.Model in order
    to provide custom fields such as
      - created_by / updated_by defining a user who made an update
      - created_at / updated_at defining a datetime when it happened

    Those fields are being set in appropriate handlers for 'pre_save' signal
    """
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   related_name="%(app_label)s_"
                                                "%(class)s_created_by+")
    created_at = models.DateTimeField()
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   related_name="%(app_label)s_"
                                                "%(class)s_updated_by+")
    updated_at = models.DateTimeField()

    class Meta:
        abstract = True
        ordering = ['updated_at', 'created_at', 'updated_by', 'created_by']
        index_together = [
            ['updated_at', 'updated_by'],
            ['created_at', 'created_by']
        ]
        get_latest_by = 'updated_at'
