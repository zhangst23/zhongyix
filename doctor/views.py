# -*- coding: utf-8 -*-

import markdown
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Doctor
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from .forms import DoctorForm

# def index(request):
# 	doctor_list = Doctor.objects.all().order_by('-created_time')
# 	return render(request, 'doctor/index.html', context={'doctor_list':doctor_list})


class IndexView(ListView):
	model = Doctor
	template_name = 'doctor/index.html'
	context_object_name = 'doctor_list'
	# 指定 paginate_by 属性后开启分页功能， 其值代表每一页包含多少篇文章
	paginate_by = 5


# def detail(request, pk):
# 	doctor = get_object_or_404(Doctor, pk=pk)
# 	doctor.wiki = markdown.markdown(doctor.wiki, extensions=[
# 																										'markdown.extensions.extra',
# 																										'markdown.extensions.codehilite',
# 																										'markdown.extensions.toc'
# 																								])

# 	context = {'doctor':doctor}
# 	return render(request, 'doctor/detail.html', context=context)


class DoctorDetailView(DetailView):
	model = Doctor
	template_name = 'doctor/detail.html'
	context_object_name = 'doctor'


# 使用 Django Form 的情况
def add_doctor(request):
	if request.method == "POST":
		doctor_form = DoctorForm(request.POST)
		if doctor_form.is_valid():
			Doctor.objects.create(
				name = doctor_form.cleaned_data['name'],
				province = doctor_form.cleaned_data['province'],
				dynastic = doctor_form.cleaned_data['dynastic'],
				wiki = doctor_form.cleaned_data['wiki'],
			)
			return HttpResponse("添加医生信息成功。")
	else:
		doctor_form = DoctorForm()
		return render(request, 'doctor/add_doctor.html', locals())





























