# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-26 13:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20160811_1953'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='receipt_id',
            field=models.CharField(max_length=100, null=True),
        ),
    ]