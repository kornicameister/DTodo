__author__ = 'Tomasz'
__doc__ = 'Model listeners'

import datetime
import logging

from django.db.models.signals import pre_save
from django.dispatch import receiver
from django_tools.middlewares import ThreadLocal

from DTodo.common.models import AuditableModel
from DTodo.models import Todo

logger = logging.getLogger(__name__)


@receiver(pre_save,
          dispatch_uid="on_auditable_model_pre_save")
def _on_auditablemodel_pre_save(**kwargs):
    """
    Handler for 'pre_save' method. This handler
    has generally no sender specified since 'DTodo.common.models.AuditableModel'
    itself is abstract model.

    Handler provide setting for following fields
        created_at, created_by
        updated_at, updated_by
    :param kwargs: all arguments as specified by pre_save
    :return: True if handled correctly, False otherwise
    """

    model = kwargs.get('instance', None)

    if not (model and isinstance(model, AuditableModel)):
        return False

    logger.info('pre_save[auditable_model=%s]' % model)

    def set_ts():
        today = datetime.datetime.today()
        if not has_id:
            model.created_at = today
        model.updated_at = today

    def set_users():
        if not has_id:
            model.created_by_id = current_user.id
        model.updated_by_id = current_user.id

    has_id = True if model.id else False
    current_user = ThreadLocal.get_current_user()

    set_ts()
    set_users()

    return True


@receiver(pre_save,
          sender=Todo,
          dispatch_uid='on_todo_pre_save')
def _on_todo_pre_save(**kwargs):
    """
    Handler for 'pre_save' signal coming from 'DTodo.models.Todo'
    in order to set 'owned_by' ref.

    :param kwargs: all arguments as specified by pre_save
    :return: True if handled correctly, False otherwise
    """
    todo = kwargs.get('instance', None)

    if not (todo and isinstance(todo, Todo) and not todo.owned_by_id):
        return False

    logger.info('pre_save[todo=%s]' % todo)

    current_user = ThreadLocal.get_current_user()
    todo.owned_by_id = current_user.id

    return True
