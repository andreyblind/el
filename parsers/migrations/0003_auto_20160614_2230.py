# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-14 22:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsers', '0002_auto_20160614_2207'),
    ]

    operations = [
        migrations.CreateModel(
            name='recipes_url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=250)),
            ],
        ),
        migrations.DeleteModel(
            name='recipes',
        ),
    ]