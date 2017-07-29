from django.contrib import admin
from .models import Zhongyao

class ZhongyaoAdmin(admin.ModelAdmin):
	list_display = ['name', 'alias', 'created_time']


admin.site.register(Zhongyao, ZhongyaoAdmin)





