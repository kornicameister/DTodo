# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('DTodo', '0004_auto_20150412_0015'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='importance',
            field=models.PositiveSmallIntegerField(validators=django.core.validators.MaxValueValidator(limit_value=10), default=1),
        ),
    ]
