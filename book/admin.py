# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Book, Book_chapter, Mulu


class BookAdmin(admin.ModelAdmin):
	list_display = ['name', 'mulu', 'created_time']
	# search_fileds = ['name',]
	list_filter = ['mulu']

class Book_capterAdmin(admin.ModelAdmin):
	list_display = ['name', 'created_time', 'book']
	# search_fileds = ['name', 'book']
	list_filter = ['book']


	class Media:
		js = (
			'/static/js/kindeditor-4.1.7/kindeditor-min.js',
			'/static/js/kindeditor-4.1.7/lang/zh_CN.js',
			'/static/js/kindeditor-4.1.7/config.js',
		)






admin.site.register(Book, BookAdmin)
admin.site.register(Book_chapter, Book_capterAdmin)
admin.site.register(Mulu)









