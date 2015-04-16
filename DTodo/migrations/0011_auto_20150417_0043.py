# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('DTodo', '0010_auto_20150415_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='importance',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]
