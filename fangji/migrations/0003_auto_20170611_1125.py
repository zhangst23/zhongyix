# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-11 03:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fangji', '0002_fangji_taboo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fangji',
            options={'verbose_name': '\u65b9\u5242', 'verbose_name_plural': '\u65b9\u5242\u5217\u8868'},
        ),
        migrations.AlterField(
            model_name='fangji',
            name='created_time',
            field=models.DateTimeField(verbose_name='\u6dfb\u52a0\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='fangji',
            name='dosage',
            field=models.TextField(verbose_name='\u5242\u91cf'),
        ),
        migrations.AlterField(
            model_name='fangji',
            name='function',
            field=models.TextField(verbose_name='\u529f\u80fd\u4e3b\u6cbb'),
        ),
        migrations.AlterField(
            model_name='fangji',
            name='name',
            field=models.CharField(max_length=100, verbose_name='\u65b9\u5242\u540d'),
        ),
        migrations.AlterField(
            model_name='fangji',
            name='prescription',
            field=models.TextField(verbose_name='\u65b9\u5242\u914d\u4f0d'),
        ),
        migrations.AlterField(
            model_name='fangji',
            name='taboo',
            field=models.TextField(verbose_name='\u7981\u5fcc'),
        ),
    ]
