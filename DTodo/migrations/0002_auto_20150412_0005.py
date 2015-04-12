# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DTodo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'get_latest_by': 'updated_at', 'ordering': ['updated_at', 'created_at', 'updated_by', 'created_by']},
        ),
        migrations.AlterModelOptions(
            name='todoitem',
            options={'get_latest_by': 'updated_at', 'ordering': ['updated_at', 'created_at', 'updated_by', 'created_by']},
        ),
        migrations.AddField(
            model_name='todo',
            name='completed',
            field=models.BooleanField(help_text='If all associated todo items are completed, todo can be marked as completed', default=False),
        ),
        migrations.AddField(
            model_name='todo',
            name='visibility',
            field=models.CharField(choices=[('PUB', 'Public'), ('PRIV', 'Private')], max_length=4, default='PRIV'),
        ),
        migrations.AlterIndexTogether(
            name='todo',
            index_together=set([('updated_at', 'updated_by'), ('created_at', 'created_by')]),
        ),
        migrations.AlterIndexTogether(
            name='todoitem',
            index_together=set([('updated_at', 'updated_by'), ('created_at', 'created_by')]),
        ),
        migrations.RemoveField(
            model_name='todoitem',
            name='disabled',
        ),
    ]
