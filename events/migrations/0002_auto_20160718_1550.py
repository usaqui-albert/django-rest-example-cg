# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-18 15:50
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userevent',
            name='key',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]