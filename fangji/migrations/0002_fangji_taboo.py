# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-10 14:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fangji', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fangji',
            name='taboo',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
