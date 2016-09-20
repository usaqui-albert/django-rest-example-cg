# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-19 22:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_event_refno_benevity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='company',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userevent',
            name='status',
            field=models.CharField(choices=[(b'A', b'ACCEPTED'), (b'R', b'REJECTED'), (b'W', b'WAITING'), (b'V', b'VIEWED'), (b'B', b'BOUNCED'), (b'E', b'EXPIRED')], default=b'W', max_length=1),
        ),
    ]
