# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-17 03:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20170316_1925'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='condition',
            field=models.CharField(default='like new', max_length=100),
            preserve_default=False,
        ),
    ]
