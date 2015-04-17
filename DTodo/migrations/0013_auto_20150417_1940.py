# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('DTodo', '0012_auto_20150417_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='tags',
            field=models.ManyToManyField(to='DTodo.Tag', blank=True,
                                         related_name='todo_tags'),
        ),
    ]
