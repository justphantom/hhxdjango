from django.contrib import admin
from .models import ProcessInfo


# Register your models here.
class ProcessInfoAdmin(admin.ModelAdmin):
    list_display = ['processno', 'processname']
    # list_editable = ['processname']
    search_fields = ["processname"]


admin.site.register(ProcessInfo, ProcessInfoAdmin)
