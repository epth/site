# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-05 11:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0005_auto_20170505_1121'),
    ]

    operations = [
        migrations.AddField(
            model_name='point',
            name='message',
            field=models.CharField(default='Idle', max_length=100),
        ),
    ]