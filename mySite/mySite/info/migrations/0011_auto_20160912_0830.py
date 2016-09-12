# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-12 08:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0010_remove_social_in_use'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='Country',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='info',
            name='city',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='info',
            name='state',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
