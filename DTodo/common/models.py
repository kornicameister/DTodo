import datetime
from django.conf import settings
from django.db import models


class AuditableModel(models.Model):
    """
    AuditableModel subclass models.Model in order
    to provide custom fields such as
      - created_by / updated_by defining a user who made an update
      - created_at / updated_at defining a datetime when it happened
    """
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   related_name="%(app_label)s_"
                                                "%(class)s_created_by")
    created_at = models.DateTimeField()
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   related_name="%(app_label)s_"
                                                "%(class)s_updated_by")
    updated_at = models.DateTimeField()

    # opposite is to create own fields and overwrite pre_save
    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        today = datetime.datetime.today()
        if not self.id:
            self.created = today
        self.modified = today
        return super(AuditableModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True
        ordering = ['updated_at', 'created_at', 'updated_by', 'created_by']
        index_together = [
            ['updated_at', 'updated_by'],
            ['created_at', 'created_by']
        ]
        get_latest_by = 'updated_at'