from django.contrib import admin
from .models import ProcessInfo, ProductInfo, ProductType


# Register your models here.
class ProcessInfoAdmin(admin.ModelAdmin):
    list_display = ['code', 'name']
    # list_editable = ['processname']
    search_fields = ["name"]


admin.site.register(ProcessInfo, ProcessInfoAdmin)
admin.site.register(ProductInfo)
admin.site.register(ProductType)
