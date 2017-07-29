from django.conf.urls import url 
from . import views

app_name = 'doctor'
urlpatterns = [
	# url(r'^$', views.index, name='index'),
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^(?P<pk>[0-9]+)/$', views.DoctorDetailView.as_view(), name='detail'),
	url(r'^add_doctor/$', views.add_doctor, name='add_doctor'),

]