# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DTodo', '0003_auto_20150412_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='todo',
            field=models.ForeignKey(related_name='todos', to='DTodo.Todo'),
        ),
    ]
