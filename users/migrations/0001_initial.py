# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-04 12:37
from __future__ import unicode_literals

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('countries', '0001_initial'),
        ('cities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('street_address', models.CharField(max_length=100)),
                ('facebook', models.CharField(max_length=100, null=True)),
                ('twitter', models.CharField(max_length=100, null=True)),
                ('linkedin', models.CharField(max_length=100, null=True)),
                ('phone_number', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=False)),
                ('free_trial_started_at', models.DateTimeField(null=True)),
                ('has_a_plan', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('city', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='city', to='cities.City')),
                ('country', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='country', to='countries.Country')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]