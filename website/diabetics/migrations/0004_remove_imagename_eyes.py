# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-05 06:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diabetics', '0003_auto_20170101_0807'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagename',
            name='eyes',
        ),
    ]