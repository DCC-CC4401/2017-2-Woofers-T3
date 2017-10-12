# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-09 20:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LeyCholito', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=200)),
                ('contrasena', models.CharField(max_length=200)),
                ('nombre', models.CharField(max_length=200)),
                ('rut', models.CharField(max_length=20)),
                ('imagen', models.FilePathField()),
                ('telefono', models.CharField(max_length=20)),
                ('correo', models.EmailField(max_length=20)),
            ],
        ),
    ]