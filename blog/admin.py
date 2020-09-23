from django.contrib import admin
from blog.models import Post, PostCategory, Comment


class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {
        'slug': ('title',)
    }
    exclude = ('creator', )

    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Post, PostModelAdmin)

class PostCategoryModelAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(PostCategory, PostCategoryModelAdmin)


class CommentModelAdmin(admin.ModelAdmin):
    list_display = ('content',)