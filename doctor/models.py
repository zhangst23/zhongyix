# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible


@python_2_unicode_compatible
class Doctor(models.Model):
	name = models.CharField(verbose_name='医生姓名', max_length=100)
	province = models.CharField(verbose_name='省份', max_length=100)
	dynastic = models.CharField(verbose_name='朝代', max_length=100)
	doctorface = models.ImageField(upload_to='doctorface', null=True, blank=True)
	created_time = models.DateTimeField(verbose_name='添加时间', null=True)
	wiki = models.TextField(verbose_name='百科')

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('doctor:detail', kwargs={'pk': self.pk})


	class Meta():
		verbose_name='名医'
		verbose_name_plural='名医列表'
