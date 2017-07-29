# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import markdown
from django.db import models
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible
from django.utils.html import strip_tags



@python_2_unicode_compatible
class Mulu(models.Model):
	name = models.CharField(verbose_name='目录', max_length=100)

	def __str__(self):
		return self.name





@python_2_unicode_compatible
class Book(models.Model):
	name = models.CharField(verbose_name='书名', max_length=100)
	mulu = models.ForeignKey(Mulu)
	created_time = models.DateTimeField(verbose_name='时间', null=True)
	author = models.CharField(verbose_name='作者', max_length=100)
	bookface = models.ImageField(upload_to='bookface', null=True, blank=True)
	content = models.TextField(verbose_name='内容')
	excerpt = models.CharField(verbose_name='摘要', max_length=200, blank=True)
	views = models.PositiveIntegerField(verbose_name='阅读量', default=0)




	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('book:detail', kwargs={'pk': self.pk}) 

	def increase_views(self):
		self.views += 1
		self.save(update_fields=['views'])

	def save(self, *args, **kwargs):
		# 如果没有写摘要
		if not self.excerpt:
			# 首先实例化一个 Markdown 类，用于渲染 body 的文本
			md = markdown.Markdown(extensions=[
				'markdown.extensions.extra',
				'markdown.extensions.codehilite',
			])
			# 先将 Markdown 文本渲染成 HTML 文本
			# strip_tags 去掉 HTML 文本的全部 HTML 标签
			# 从文本摘取前 54 个字符赋给 excerpt
			self.excerpt = strip_tags(md.convert(self.content))[:54]

		# 调用父类的 save 方法将数据保存到数据库中
		super(Book, self).save(*args, **kwargs)


	class Meta:
		verbose_name = '书籍'
		verbose_name_plural = '书籍列表'








@python_2_unicode_compatible
class Book_chapter(models.Model):
	name = models.CharField(verbose_name='章节名', max_length=140)
	book = models.ForeignKey('Book')
	# book_name = models.ForeignKey('Book', related_name='name', verbose_name='所属图书')
	created_time = models.DateTimeField(verbose_name='时间')
	content = models.TextField(verbose_name='内容')


	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('book:content', kwargs={'pk': self.pk})

	class Meta:
		verbose_name = '图书章节'
		verbose_name_plural = '图书章节列表'














