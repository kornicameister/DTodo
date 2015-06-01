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
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False,
                                        verbose_name='ID', auto_created=True)),
                ('word', models.CharField(unique=True, max_length=15)),
                ('details', models.TextField(null=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False,
                                        verbose_name='ID', auto_created=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('name', models.CharField(max_length=15)),
                ('completed', models.BooleanField(default=False)),
                ('visibility', models.CharField(max_length=4, default='PRIV',
                                                choices=[('PUB',
                                                          'visibility.public'),
                                                         ('PRIV',
                                                          'visibility.private')])),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                                 related_name='dtodo_todo_created_by+')),
            ],
            options={
                'ordering': ['updated_at', 'created_at', 'updated_by',
                             'created_by'],
                'abstract': False,
                'get_latest_by': 'updated_at',
            },
        ),
        migrations.CreateModel(
            name='TodoItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False,
                                        verbose_name='ID', auto_created=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('title', models.CharField(max_length=15)),
                ('description', models.TextField(max_length=45)),
                ('done', models.BooleanField(default=False)),
                ('importance', models.PositiveSmallIntegerField(default=1)),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                                 related_name='dtodo_todoitem_created_by+')),
                ('todo', models.ForeignKey(to='DTodo.Todo')),
                ('updated_by', models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                                 related_name='dtodo_todoitem_updated_by+')),
            ],
            options={
                'ordering': ['updated_at', 'created_at', 'updated_by',
                             'created_by'],
                'abstract': False,
                'get_latest_by': 'updated_at',
            },
        ),
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False,
                                        verbose_name='ID', auto_created=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('name', models.CharField(max_length=15)),
                ('visibility', models.CharField(max_length=4, default='PRIV',
                                                choices=[('PUB',
                                                          'visibility.public'),
                                                         ('PRIV',
                                                          'visibility.private'),
                                                         ('SHRD',
                                                          'visibility.shared')])),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                                 related_name='dtodo_todolist_created_by+')),
                ('owned_by', models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                               related_name='+')),
                ('updated_by', models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                                 related_name='dtodo_todolist_updated_by+')),
            ],
            options={
                'ordering': ['updated_at', 'created_at', 'updated_by',
                             'created_by'],
                'abstract': False,
                'get_latest_by': 'updated_at',
            },
        ),
        migrations.AddField(
            model_name='todo',
            name='list',
            field=models.ForeignKey(to='DTodo.TodoList',
                                    related_name='todo_list'),
        ),
        migrations.AddField(
            model_name='todo',
            name='owned_by',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                    related_name='+'),
        ),
        migrations.AddField(
            model_name='todo',
            name='tags',
            field=models.ManyToManyField(to='DTodo.Tag', blank=True,
                                         related_name='todo_tags'),
        ),
        migrations.AddField(
            model_name='todo',
            name='updated_by',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                    related_name='dtodo_todo_updated_by+'),
        ),
        migrations.AlterIndexTogether(
            name='todolist',
            index_together=set(
                [('updated_at', 'updated_by'), ('created_at', 'created_by')]),
        ),
        migrations.AlterIndexTogether(
            name='todoitem',
            index_together=set(
                [('updated_at', 'updated_by'), ('created_at', 'created_by')]),
        ),
        migrations.AlterIndexTogether(
            name='todo',
            index_together=set(
                [('updated_at', 'updated_by'), ('created_at', 'created_by')]),
        ),
    ]
