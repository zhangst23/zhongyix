# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible



@python_2_unicode_compatible
class Zhongyao(models.Model):
	name = models.CharField(verbose_name='中药名称', max_length=100)
	name_en = models.CharField(max_length=150)
	alias = models.CharField(verbose_name='别名', max_length=200)
	area = models.TextField()
	shape = models.TextField()
	distinguish = models.TextField()
	xingwei = models.TextField()
	guijing = models.TextField()
	function = models.TextField()
	chemical = models.TextField()
	pharmacology = models.TextField()
	dosage = models.TextField()
	storage = models.TextField()
	created_time = models.DateTimeField(verbose_name='添加时间')

	def __str__(self):
		return self.name;


	def get_absolute_url(self):
		return reverse('zhongyao:detail', kwargs={'pk': self.pk})


	class Meta:
		verbose_name = '中药'
		verbose_name_plural = '中药列表'

















