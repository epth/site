# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-17 17:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0003_auto_20170417_0845'),
    ]

    operations = [
        migrations.RenameField(
            model_name='point',
            old_name='point_map',
            new_name='map_id',
        ),
    ]
