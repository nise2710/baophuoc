from django.contrib import admin
from thongtin.models import *

class ThongtinCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'tag']

class ThongtinDBAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date', 'display', 'url_tag', 'views')

# Register your models here.
admin.site.register(ThongtinCategory, ThongtinCategoryAdmin)
admin.site.register(ThongtinDB, ThongtinDBAdmin)