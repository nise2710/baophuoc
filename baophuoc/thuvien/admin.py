from django.contrib import admin
from thuvien.models import ThuvienCategory, ContentVideo, ContentPhoto, ContentPhotoLink

class ThuvienCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'tag']

class ContentVideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'date', 'display', 'url_tag', 'views')
    
class LinkInline(admin.StackedInline):
    model = ContentPhotoLink
    extra = 3

class ContentPhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'date', 'display', 'url_tag', 'views')
    inlines = [LinkInline]

# Register your models here.
admin.site.register(ThuvienCategory, ThuvienCategoryAdmin)
admin.site.register(ContentVideo, ContentVideoAdmin)
admin.site.register(ContentPhoto, ContentPhotoAdmin)
