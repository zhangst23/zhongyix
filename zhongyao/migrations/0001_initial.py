# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-10 13:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Zhongyao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('name_en', models.CharField(max_length=150)),
                ('alias', models.CharField(max_length=200)),
                ('area', models.TextField()),
                ('shape', models.TextField()),
                ('distinguish', models.TextField()),
                ('xingwei', models.TextField()),
                ('guijing', models.TextField()),
                ('function', models.TextField()),
                ('chemical', models.TextField()),
                ('pharmacology', models.TextField()),
                ('dosage', models.TextField()),
                ('storage', models.TextField()),
                ('created_time', models.DateTimeField()),
            ],
        ),
    ]
