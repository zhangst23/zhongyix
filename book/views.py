# -*- coding: utf-8 -*-

import markdown
from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Book, Book_chapter, Mulu
from .forms import BookForm

def index(request):
	book_list = Book.objects.all().order_by('-created_time')

	paginator = Paginator(book_list, 2) #每页显示5个联系人

	page = request.GET.get('page', 1)
	try:
		book_list = paginator.page(page)
	except PageNotAnInteger:
		# 如果用户请求的页码号不是整数，显示第一页
		book_list = paginator.page(1)
	except EmptyPage:
		book_list = paginator.page(paginator.num_pages)

	return render(request, 'book/index.html', context={'book_list':book_list})










def detail(request, pk):
	book = get_object_or_404(Book, pk=pk)
	
	# 阅读量+1
	book.increase_views()

	book.content = markdown.markdown(book.content, extensions=[
																										'markdown.extensions.extra',
																										'markdown.extensions.codehilite',
																										'markdown.extensions.toc'
																								])

	book_chapter_list = book.book_chapter_set.all() 
	context = {'book':book, 'book_chapter_list':book_chapter_list}
	return render(request, 'book/detail.html', context=context)



def content(request, pk):
	book_chapter = get_object_or_404(Book_chapter, pk=pk)
	book_chapter.content = markdown.markdown(book_chapter.content, extensions=[
																										'markdown.extensions.extra',
																										'markdown.extensions.codehilite',
																										'markdown.extensions.toc'
																								])
	context = {'book_chapter':book_chapter, 'book_chapter.content':book_chapter.content}
	return render(request, 'book/content.html', context=context)



def add_book(request):
	if request.method == "POST":
		book_form = BookForm(request.POST)
		if book_form.is_valid():
			book_form.save()
			return HttpResponse("添加图书信息成功！")
	else:
		book_form = BookForm()
	return render(request, 'book/add_book.html', locals())





def mulu(request, pk):
	mulu = get_object_or_404(Mulu, pk=pk)
	book_list = Book.objects.filter(mulu=mulu).order_by('-created_time')
	return render(request, 'book/index.html', context={'book_list':book_list})





















