from django.contrib import admin
from .models import BookInfo, Chapter, Author

# Register your models here.
admin.site.register(BookInfo)
admin.site.register(Chapter)
admin.site.register(Author)
