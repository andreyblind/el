# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-14 22:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipes',
            name='url',
            field=models.CharField(max_length=200),
        ),
    ]
