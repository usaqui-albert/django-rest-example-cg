# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-09 20:01
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_added_to_benevity'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='benevity_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]