# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-13 00:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LeyCholito', '0008_auto_20171012_2355'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Usuario',
            new_name='UserInfo',
        ),
    ]