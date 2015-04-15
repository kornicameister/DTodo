# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('DTodo', '0007_auto_20150415_0112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_by',
            field=models.ForeignKey(related_name='dtodo_todo_created_by+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='todo',
            name='owned_by',
            field=models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='todo',
            name='updated_by',
            field=models.ForeignKey(related_name='dtodo_todo_updated_by+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='created_by',
            field=models.ForeignKey(related_name='dtodo_todoitem_created_by+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='todo',
            field=models.ForeignKey(to='DTodo.Todo'),
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='updated_by',
            field=models.ForeignKey(related_name='dtodo_todoitem_updated_by+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='created_by',
            field=models.ForeignKey(related_name='dtodo_todolist_created_by+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='updated_by',
            field=models.ForeignKey(related_name='dtodo_todolist_updated_by+', to=settings.AUTH_USER_MODEL),
        ),
    ]
