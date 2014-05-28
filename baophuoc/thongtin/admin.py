from django.contrib import admin
from thongtin.models import Category, Content

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date', 'display')

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Content, ContentAdmin)