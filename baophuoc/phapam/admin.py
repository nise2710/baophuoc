from django.contrib import admin
from phapam.models import PhapamCategory, PhapamDB

class PhapamCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'tag']

class PhapamDBAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'date', 'display', 'url_tag', 'views')

# Register your models here.
admin.site.register(PhapamCategory, PhapamCategoryAdmin)
admin.site.register(PhapamDB, PhapamDBAdmin)