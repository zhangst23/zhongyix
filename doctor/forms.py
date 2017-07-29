# -*- coding: utf-8 -*-
from django import forms

class DoctorForm(forms.Form):
	name = forms.CharField(label='医生姓名')
	province = forms.CharField(label='省份')
	dynastic = forms.CharField(label='朝代')
	wiki = forms.CharField(label='人物介绍')

	# name = forms.CharField(label='医生姓名', error_message={"required":"这项必须填写"})