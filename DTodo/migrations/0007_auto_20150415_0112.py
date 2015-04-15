# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('DTodo', '0006_auto_20150412_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='todo',
            name='list',
            field=models.OneToOneField(related_name='todo_list',
                                       to='DTodo.TodoList', null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='name',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='todo',
            name='visibility',
            field=models.CharField(choices=[('PUB', 'visibility.public'),
                                            ('PRIV', 'visibility.private')],
                                   default='PRIV', max_length=4),
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='description',
            field=models.TextField(max_length=45),
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='done',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='title',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='visibility',
            field=models.CharField(choices=[('PUB', 'visibility.public'),
                                            ('PRIV', 'visibility.private'),
                                            ('SHRD', 'visibility.shared')],
                                   default='PRIV', max_length=4),
        ),
    ]
