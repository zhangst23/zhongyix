# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-10 14:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='fangji',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('prescription', models.TextField()),
                ('function', models.TextField()),
                ('dosage', models.TextField()),
                ('created_time', models.DateTimeField()),
            ],
        ),
    ]
