# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('DTodo', '0014_auto_20150417_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='list',
            field=models.ForeignKey(to='DTodo.TodoList',
                                    related_name='todo_list', blank=True,
                                    null=True),
        ),
    ]
