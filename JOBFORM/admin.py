from django.contrib import admin
from .models import JobApplication,JobPost


# Register your models here.

class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'applied_on')

class JobPostAdmin(admin.ModelAdmin):
     list_display = ('title', 'location', 'posted_on')


admin.site.register(JobApplication,JobApplicationAdmin)
admin.site.register(JobPost,JobPostAdmin)