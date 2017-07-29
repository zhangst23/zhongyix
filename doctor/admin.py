from django.contrib import admin
from .models import Doctor

class DoctorAdmin(admin.ModelAdmin):
	list_display = ['name', 'province', 'dynastic', 'created_time']



admin.site.register(Doctor, DoctorAdmin)