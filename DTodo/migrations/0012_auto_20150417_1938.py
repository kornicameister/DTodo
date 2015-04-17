# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('DTodo', '0011_auto_20150417_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='tags',
            field=models.ManyToManyField(null=True, to='DTodo.Tag',
                                         related_name='todo_tags'),
        ),
    ]
