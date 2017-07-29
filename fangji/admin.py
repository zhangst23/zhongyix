from django.contrib import admin
from .models import Fangji

class FangjiAdmin(admin.ModelAdmin):
	list_display = ['name', 'created_time']


	class Media:
		js = (
			'/static/js/kindeditor-4.1.7/kindeditor-min.js',
			'/static/js/kindeditor-4.1.7/lang/zh_CN.js',
			'/static/js/kindeditor-4.1.7/config.js',
		)







admin.site.register(Fangji, FangjiAdmin)