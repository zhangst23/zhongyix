# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-09 13:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_book_created_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book_chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter', models.CharField(max_length=140)),
                ('content', models.TextField()),
                ('created_time', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book_chapter',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.Book'),
        ),
    ]
