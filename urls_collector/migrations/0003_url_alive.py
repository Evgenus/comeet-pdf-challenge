# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-20 18:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urls_collector', '0002_auto_20180120_1947'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='alive',
            field=models.BooleanField(default=False),
        ),
    ]
