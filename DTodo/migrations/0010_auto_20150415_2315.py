# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('DTodo', '0009_auto_20150415_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='list',
            field=models.ForeignKey(related_name='todo_list',
                                    to='DTodo.TodoList', null=True),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='name',
            field=models.CharField(max_length=15),
        ),
    ]
