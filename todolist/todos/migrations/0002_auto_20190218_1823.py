# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-02-18 18:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='is_done',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 18, 18, 23, 6, 277628)),
        ),
    ]
