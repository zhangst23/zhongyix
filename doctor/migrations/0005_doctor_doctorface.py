# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-08 14:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0004_auto_20170612_2328'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='doctorface',
            field=models.ImageField(blank=True, null=True, upload_to='doctorface'),
        ),
    ]