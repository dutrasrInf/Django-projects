# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-12 08:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0011_auto_20160912_0830'),
    ]

    operations = [
        migrations.RenameField(
            model_name='info',
            old_name='Country',
            new_name='country',
        ),
    ]
