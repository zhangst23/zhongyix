# -*- coding: utf-8 -*-
from django import forms
from .models import Book

class BookForm(forms.ModelForm):

	class Meta:
		model = Book
		exclude = ("id", "created_time", "excerpt", "views",)
