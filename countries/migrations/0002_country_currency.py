# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-01 23:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='currency',
            field=models.CharField(default='cad', max_length=3),
            preserve_default=False,
        ),
    ]