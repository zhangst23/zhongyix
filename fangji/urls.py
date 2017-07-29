from django.conf.urls import url 
from . import views

app_name = 'fangji'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<pk>[0-9]+)/$', views.detail, name='detail'),
	url(r'^add_fangji/$', views.add_fangji, name='add_fangji'),
]