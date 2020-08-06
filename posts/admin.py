from django.contrib import admin

from .models import Post, Category, Tag


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time',
                    'modified_time', 'category', 'author']
    fields = ['title', 'body', 'excerpt', 'category', 'tags']
    search_fields = ['title', 'body', 'excerpt']
    list_filter = ['category']

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)


# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
