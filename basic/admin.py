from django.contrib import admin
from .models import ProcessInfo


# Register your models here.
class ProcessInfoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProcessInfo._meta.get_fields()]


admin.site.register(ProcessInfo, ProcessInfoAdmin)
