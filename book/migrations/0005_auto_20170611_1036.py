# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-11 02:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_auto_20170609_2125'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': '\u4e66\u7c4d', 'verbose_name_plural': '\u4e66\u7c4d\u5217\u8868'},
        ),
        migrations.AlterModelOptions(
            name='book_chapter',
            options={'verbose_name': '\u56fe\u4e66\u7ae0\u8282', 'verbose_name_plural': '\u56fe\u4e66\u7ae0\u8282\u5217\u8868'},
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=100, verbose_name='\u4f5c\u8005'),
        ),
        migrations.AlterField(
            model_name='book',
            name='content',
            field=models.TextField(verbose_name='\u5185\u5bb9'),
        ),
        migrations.AlterField(
            model_name='book',
            name='created_time',
            field=models.DateTimeField(verbose_name='\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='book',
            name='mulu',
            field=models.CharField(max_length=150, verbose_name='\u76ee\u5f55'),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=100, verbose_name='\u4e66\u540d'),
        ),
        migrations.AlterField(
            model_name='book_chapter',
            name='content',
            field=models.TextField(verbose_name='\u5185\u5bb9'),
        ),
        migrations.AlterField(
            model_name='book_chapter',
            name='created_time',
            field=models.DateTimeField(verbose_name='\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='book_chapter',
            name='name',
            field=models.CharField(max_length=140, verbose_name='\u7ae0\u8282\u540d'),
        ),
    ]