# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible

@python_2_unicode_compatible
class Fangji(models.Model):
	name = models.CharField(verbose_name='方剂名', max_length=100)
	prescription = models.TextField(verbose_name='方剂组成')
	function = models.TextField(verbose_name='功能主治')
	dosage = models.TextField(verbose_name='剂量')
	taboo = models.TextField(verbose_name='禁忌')
	created_time = models.DateTimeField(verbose_name='添加时间', null=True)


	def __str__(self):
		return self.name;

	def get_absolute_url(self):
		return reverse('fangji:detail', kwargs={'pk': self.pk})


	class Meta:
		verbose_name = '方剂'
		verbose_name_plural = '方剂列表'
