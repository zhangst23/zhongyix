# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-11 03:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0002_doctor_created_time'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='doctor',
            options={'verbose_name': '\u540d\u533b', 'verbose_name_plural': '\u540d\u533b\u5217\u8868'},
        ),
        migrations.AlterField(
            model_name='doctor',
            name='created_time',
            field=models.DateTimeField(verbose_name='\u6dfb\u52a0\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='dynastic',
            field=models.CharField(max_length=100, verbose_name='\u671d\u4ee3'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='name',
            field=models.CharField(max_length=100, verbose_name='\u533b\u751f\u59d3\u540d'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='province',
            field=models.CharField(max_length=100, verbose_name='\u7701\u4efd'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='wiki',
            field=models.TextField(verbose_name='\u767e\u79d1'),
        ),
    ]
