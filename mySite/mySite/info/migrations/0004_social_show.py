# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-10 07:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0003_auto_20160910_0728'),
    ]

    operations = [
        migrations.AddField(
            model_name='social',
            name='show',
            field=models.BooleanField(default=False),
        ),
    ]
