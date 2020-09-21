from django.contrib import admin
from accounts.models import Profile

# Register your models here.
class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ('function', 'gender')

admin.site.register(Profile, ProfileModelAdmin)