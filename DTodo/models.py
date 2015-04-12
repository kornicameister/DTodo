from django.conf import settings
from django.db import models
from django.core import validators
from django.utils.translation import ugettext_lazy as _
from DTodo.common.models import AuditableModel

'''

models.OneToOneField is similar to models.ForeignKey(unique=True) but
difference is that with reverse relation method with ForeignKey will
return QuerySet

'''


class Tag(models.Model):
    """
    Each todo can be associated with tag, therefore it is easily
    accessible over custom name
    """
    word = models.CharField(max_length=15, unique=True)
    """
    word describes the content of the tag, therefore the verbose short version
    """
    details = models.TextField(max_length=100, null=True)
    """
    details can be used to describe something more beyond the tag
    """

    def has_details(self):
        """
        Determines if tag has details describing it
        """
        return True if self.details else False


class TodoList(AuditableModel):
    PUBLIC_VISIBILITY = 'PUB'
    PRIVATE_VISIBILITY = 'PRIV'
    SHARED_VISIBILITY = 'SHRD'
    VISIBILITY = (
        (PUBLIC_VISIBILITY, _('Public')),
        (PRIVATE_VISIBILITY, _('Private')),
        (SHARED_VISIBILITY, _('Shared'))
    )
    """
    Wraps several todos in the single list. Note that this is different
    level of aggregation, other then Tag.
    """
    name = models.CharField(max_length=15, null=False, unique=False,
                            help_text=_('Title of Todo list'))
    """
    TodoList has a name, this name is considered unique within given user
    namespace of all todos
    """
    visibility = models.CharField(max_length=4, choices=VISIBILITY,
                                  default=PRIVATE_VISIBILITY)
    """
    Visibility markdown a list as public, private or shared.
    Note that visiblity level has precedence over Todo visibility.
    In other words if list is private therefore all todos are considered
    private.
    User can have list in following fashion:
    - 1 private
    - 1 shared
    - unlimited public
    """
    owned_by = models.ForeignKey(settings.AUTH_USER_MODEL)
    """
    Marks down a user that created a todo and is an owner of such todo.
    Note that some properties of todo list are unique in the namespace
    of the single user.
    """
    pass


class Todo(AuditableModel):
    # visibilite
    PUBLIC_VISIBILITY = 'PUB'
    PRIVATE_VISIBILITY = 'PRIV'
    VISIBILITY = (
        (PUBLIC_VISIBILITY, _('Public')),
        (PRIVATE_VISIBILITY, _('Private'))
    )
    # visibility
    # fields
    name = models.CharField(max_length=15, null=False, unique=False,
                            help_text=_('Title of single Todo'))
    completed = models.BooleanField(null=False, default=False, help_text=_(
        'If all associated todo items are'
        ' completed, todo can be marked as completed')
    )
    visibility = models.CharField(max_length=4, choices=VISIBILITY,
                                  default=PRIVATE_VISIBILITY)
    tags = models.ManyToManyField(Tag, related_name='todo_tags')
    """
    Multiple tags can be associated with a Todo
    """
    list = models.OneToOneField(TodoList, related_name='todo_list')
    """
    Todo belong only to single list
    """
    owned_by = models.ForeignKey(settings.AUTH_USER_MODEL)
    """
    Todo is owner by some user. This is different scope then user who could
    create a list todo is in because list could be public or shared therefore
    visible by other users
    """
    # fields

    def is_public(self):
        return self.visibility == self.public_visibility()

    def is_private(self):
        return not self.is_public()

    def is_visible(self):
        return self.is_public()

    def is_completed(self):
        return self.completed

    def can_complete(self):
        todos = self.todos.filter(done=False)
        can_complete = len(todos) == 0
        return can_complete

    @staticmethod
    def private_visibility():
        """
        Returns internal marker for Todo which is private
        """
        return Todo.PRIVATE_VISIBILITY

    @staticmethod
    def public_visibility():
        """
        Returns internal marker for Todo which is public
        """
        return Todo.PUBLIC_VISIBILITY


class TodoItem(AuditableModel):
    MAX_IMPORTANCE = 10

    # fields
    todo = models.ForeignKey(Todo, related_name='todos')
    title = models.CharField(max_length=15, null=False, unique=False,
                             help_text=_('Title of todo item'))
    description = models.TextField(max_length=450, help_text=_(
        'Description of what is to be done for todo'))
    done = models.BooleanField(null=False, default=False,
                               help_text=_('Marks todo as done or note'))
    """
    Each todo has a list of tasks [TodoItem] to complete in order to complete
    a todo itself. This property [done] uniquely describes an item
    as completed or not
    """
    importance = models.PositiveSmallIntegerField(
        default=1,
        validators=validators.MaxValueValidator(limit_value=MAX_IMPORTANCE))
    """
    Used to order the items on the list from the most to less important one.
    Importance determines which todos are supposed to be handled by the
    assigned user in the first place
    """
    # fields

    def mark_done(self):
        self.done = True

    def mark_not_done(self):
        self.done = False

    def is_visible(self):
        todo = self.todo
        if todo is None:
            raise RuntimeError('TodoItem should be associated with Todo')
        return todo.is_visible()
