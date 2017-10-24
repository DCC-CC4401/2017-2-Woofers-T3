# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-23 13:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LeyCholito', '0009_auto_20171013_0020'),
    ]

    operations = [
        migrations.CreateModel(
            name='FichaAnimal',
            fields=[
                ('nombre', models.CharField(max_length=20)),
                ('edad', models.CharField(max_length=20)),
                ('tiempo', models.CharField(max_length=20)),
                ('denuncia', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='LeyCholito.Denuncia')),
            ],
        ),
    ]