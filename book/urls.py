# -*- coding: utf-8 -*-

from django.conf.urls import url 
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'book'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^book/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
	url(r'^book/content/(?P<pk>[0-9]+)/$', views.content, name='content'),
	url(r'^book/add_book/$', views.add_book, name='add_book'),
	url(r'^book/mulu/(?P<pk>[0-9]+)/$', views.mulu, name='mulu'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
