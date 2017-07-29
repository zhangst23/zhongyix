# -*- coding: utf-8 -*-

import markdown
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from .models import Fangji


def index(request):
	fangji_list = Fangji.objects.all().order_by('-created_time')

	paginator = Paginator(fangji_list, 2)
	page = request.GET.get('page')

	try:
		fangji_list = paginator.page(page)
	except PageNotAnInteger:
		fangji_list = paginator.page(1)
	except EmptyPage:
		fangji_list = paginator.page(paginator.num_pages)


	return render(request, 'fangji/index.html', context={'fangji_list':fangji_list})


def detail(request, pk):
	fangji = get_object_or_404(Fangji, pk=pk)
	fangji.prescription = markdown.markdown(fangji.prescription, extensions=[
																										'markdown.extensions.extra',
																										'markdown.extensions.codehilite',
																										'markdown.extensions.toc'
																								])
	fangji.function = markdown.markdown(fangji.function, extensions=[
																										'markdown.extensions.extra',
																										'markdown.extensions.codehilite',
																										'markdown.extensions.toc'
																								])

	fangji.dosage = markdown.markdown(fangji.dosage, extensions=[
																										'markdown.extensions.extra',
																										'markdown.extensions.codehilite',
																										'markdown.extensions.toc'
																								])
	context = {'fangji':fangji}
	return render(request, 'fangji/detail.html', context=context)


# 不知道为什么老出错：TemplateDoesNotExist at /fangji/add_fangji/
def add_fangji(request):
	if request.method == "POST":
		name = request.POST['name']
		prescription = request.POST['prescription']
		function = request.POST['function']
		dosage = request.POST['dosage']
		taboo = request.POST['taboo']
		# 然后把接收的数据放数据库里
		Fangji.objects.create(
			name = name,
			prescription = prescription,
			function = function,
			dosage = dosage,
			taboo = taboo,
		)
		return HttpResponse("添加方剂信息成功。")
	else:
		return render(request, 'fangji/add_fangji.html', locals())













