# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-06 09:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_confirmstring'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='has_confirmed',
            field=models.BooleanField(default=False),
        ),
    ]
