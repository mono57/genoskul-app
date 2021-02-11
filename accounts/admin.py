from django.contrib import admin
from accounts.models import Speciality, Profile, Profession, SchoolStudentLevel

# Register your models here.


class SchoolStudentLevelModelAdmin(admin.ModelAdmin):
    list_display = ('level', 'description')


admin.site.register(SchoolStudentLevel, SchoolStudentLevelModelAdmin)


class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ('gender', 'profession')


admin.site.register(Profile, ProfileModelAdmin)


class SpecialityModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


admin.site.register(Speciality, SpecialityModelAdmin)


admin.site.register(Profession)