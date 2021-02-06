from django.contrib import admin
from accounts.models import SchoolStudentProfile, Speciality, StudentProfile

# Register your models here.


class StudentProfileModelAdmin(admin.ModelAdmin):
    list_display = ('gender', 'speciality')


admin.site.register(StudentProfile, StudentProfileModelAdmin)


class SchoolStudentProfileModelAdmin(admin.ModelAdmin):
    list_display = ('gender', 'level')


admin.site.register(SchoolStudentProfile, SchoolStudentProfileModelAdmin)


class SpecialityModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


admin.site.register(Speciality, SpecialityModelAdmin)
