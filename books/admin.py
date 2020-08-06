from django.contrib import admin
from .models import BookInfo, Chapter, Author


# Register your models here.
class ChapterAdmin(admin.ModelAdmin):
    search_fields = ["body", "title"]


admin.site.register(BookInfo)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Author)
