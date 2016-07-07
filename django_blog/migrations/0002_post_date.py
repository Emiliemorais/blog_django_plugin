# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-07 00:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('django_blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 7, 7, 0, 0, 9, 730578, tzinfo=utc)),
            preserve_default=False,
        ),
    ]