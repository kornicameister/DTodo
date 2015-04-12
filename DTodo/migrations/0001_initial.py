# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('name', models.CharField(help_text='Title of single Todo', unique=True, max_length=15)),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='dtodo_todo_created_by')),
                ('updated_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='dtodo_todo_updated_by')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TodoItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('title', models.CharField(help_text='Title of todo item', max_length=15)),
                ('description', models.TextField(help_text='Description of what is to be done for todo', max_length=450)),
                ('done', models.BooleanField(default=False, help_text='Marks todo as done or note')),
                ('disabled', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='dtodo_todoitem_created_by')),
                ('todo', models.OneToOneField(to='DTodo.Todo')),
                ('updated_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='dtodo_todoitem_updated_by')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
