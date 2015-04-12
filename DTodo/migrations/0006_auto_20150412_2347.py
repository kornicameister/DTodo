# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('DTodo', '0005_todoitem_importance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('word', models.CharField(max_length=15, unique=True)),
                ('details', models.TextField(null=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('name', models.CharField(help_text='Title of Todo list', max_length=15)),
                ('visibility', models.CharField(choices=[('PUB', 'Public'), ('PRIV', 'Private'), ('SHRD', 'Shared')], default='PRIV', max_length=4)),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='dtodo_todolist_created_by')),
                ('owned_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='dtodo_todolist_updated_by')),
            ],
            options={
                'ordering': ['updated_at', 'created_at', 'updated_by', 'created_by'],
                'get_latest_by': 'updated_at',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='todo',
            name='owned_by',
            field=models.ForeignKey(default=-1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='todo',
            name='name',
            field=models.CharField(help_text='Title of single Todo', max_length=15),
        ),
        migrations.AddField(
            model_name='todo',
            name='list',
            field=models.OneToOneField(default=-1, to='DTodo.TodoList', related_name='todo_list'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='todo',
            name='tags',
            field=models.ManyToManyField(related_name='todo_tags', to='DTodo.Tag'),
        ),
        migrations.AlterIndexTogether(
            name='todolist',
            index_together=set([('created_at', 'created_by'), ('updated_at', 'updated_by')]),
        ),
    ]
