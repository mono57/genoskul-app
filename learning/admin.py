from django.contrib import admin
from learning.models import *



class DocumentModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'download_count', 'user')


admin.site.register(Document, DocumentModelAdmin)

admin.site.register(DocumentType)
admin.site.register(DocumentCategory)