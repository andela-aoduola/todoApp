# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-02 04:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TodoItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('due_at', models.DateTimeField(verbose_name='due date')),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=100)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='todolists', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='todoitem',
            name='todolist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='todolists.TodoList'),
        ),
    ]
