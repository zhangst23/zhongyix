# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-11 03:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhongyao', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='zhongyao',
            options={'verbose_name': '\u4e2d\u836f', 'verbose_name_plural': '\u4e2d\u836f\u5217\u8868'},
        ),
        migrations.AlterField(
            model_name='zhongyao',
            name='alias',
            field=models.CharField(max_length=200, verbose_name='\u522b\u540d'),
        ),
        migrations.AlterField(
            model_name='zhongyao',
            name='created_time',
            field=models.DateTimeField(verbose_name='\u6dfb\u52a0\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='zhongyao',
            name='name',
            field=models.CharField(max_length=100, verbose_name='\u4e2d\u836f\u540d\u79f0'),
        ),
    ]
