from django.contrib import admin
from phathoc.models import PhathocCategory, PhathocDB

class PhathocCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'tag']

class PhathocDBAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date', 'display', 'url_tag', 'views')

# Register your models here.
admin.site.register(PhathocCategory, PhathocCategoryAdmin)
admin.site.register(PhathocDB, PhathocDBAdmin)