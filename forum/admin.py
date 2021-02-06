from django.contrib import admin

from forum.models import *

class ForumModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

admin.site.register(Forum, ForumModelAdmin)
admin.site.register(ForumRegistration)
admin.site.register(Topic)
admin.site.register(Comment)