from django.contrib import admin

# Register your models here.
from jobs.models import *


class ResumeModelAdmin(admin.ModelAdmin):
    list_display = ('pro_title', 'location', )

admin.site.register(Resume, ResumeModelAdmin)

class JobModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'closing_date')

admin.site.register(Job, JobModelAdmin)

admin.site.register(JobType)
admin.site.register(JobCategory)