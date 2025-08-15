from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import JobApplication, JobPost


# JobApplication Admin
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'applied_on')


# JobPost Admin with Import/Export
@admin.register(JobPost)
class JobPostAdmin(ImportExportModelAdmin):
    list_display = ('title', 'location', 'posted_on')


# Register JobApplication
admin.site.register(JobApplication, JobApplicationAdmin)
