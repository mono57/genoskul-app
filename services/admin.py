from django.contrib import admin

# Register your models here.
from services.models import *

class BoxModelAdmin(admin.ModelAdmin):
    list_display = ('struct_name', 'confirmed')
    search_fields = ('struct_name', 'type', 'struct_description', 'address')
    list_filter = ('confirmed', )


admin.site.register(Box, BoxModelAdmin)

admin.site.register(BoxType)