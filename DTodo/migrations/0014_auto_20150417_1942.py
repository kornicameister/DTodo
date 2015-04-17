# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('DTodo', '0013_auto_20150417_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='list',
            field=models.ForeignKey(blank=True, default=1,
                                    related_name='todo_list',
                                    to='DTodo.TodoList'),
            preserve_default=False,
        ),
    ]
