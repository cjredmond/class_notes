# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-14 15:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20161014_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='fav_snack',
            field=models.CharField(max_length=25, null=True),
        ),
    ]
