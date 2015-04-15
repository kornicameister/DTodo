# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('DTodo', '0008_auto_20150415_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='owned_by',
            field=models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL),
        ),
    ]
