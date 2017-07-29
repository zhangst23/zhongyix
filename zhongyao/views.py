# -*- coding: utf-8 -*-

import markdown
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from .models import Zhongyao


def index(request):
	zhongyao_list = Zhongyao.objects.all().order_by('-created_time')

	paginator = Paginator(zhongyao_list, 2) #每页显示5个联系人

	page = request.GET.get('page', 1)
	try:
		zhongyao_list = paginator.page(page)
	except PageNotAnInteger:
		# 如果用户请求的页码号不是整数，显示第一页
		zhongyao_list = paginator.page(1)
	except EmptyPage:
		zhongyao_list = paginator.page(paginator.num_pages)
	return render(request, 'zhongyao/index.html', context={'zhongyao_list':zhongyao_list})

def detail(request, pk):
	zhongyao = get_object_or_404(Zhongyao, pk=pk)
	zhongyao.shape = markdown.markdown(zhongyao.shape, extensions=[
																										'markdown.extensions.extra',
																										'markdown.extensions.codehilite',
																										'markdown.extensions.toc'
																								])
	zhongyao.distinguish = markdown.markdown(zhongyao.distinguish, extensions=[
																										'markdown.extensions.extra',
																										'markdown.extensions.codehilite',
																										'markdown.extensions.toc'
																								])
	zhongyao.function = markdown.markdown(zhongyao.function, extensions=[
																										'markdown.extensions.extra',
																										'markdown.extensions.codehilite',
																										'markdown.extensions.toc'
																								])
	zhongyao.chemical = markdown.markdown(zhongyao.chemical, extensions=[
																										'markdown.extensions.extra',
																										'markdown.extensions.codehilite',
																										'markdown.extensions.toc'
																							])
	zhongyao.pharmacology = markdown.markdown(zhongyao.pharmacology, extensions=[
																										'markdown.extensions.extra',
																										'markdown.extensions.codehilite',
																										'markdown.extensions.toc'
																								])

	context = {'zhongyao':zhongyao}
	return render(request, 'zhongyao/detail.html', context=context)
















