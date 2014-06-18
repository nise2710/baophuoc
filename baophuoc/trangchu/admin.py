from django.contrib import admin
from trangchu.models import *

class TrangchuCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'tag']
    
class SlideLinkInline(admin.StackedInline):
    model = SlideLink
    extra = 5

class SlidePhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'date', 'display', 'url_tag', 'views')
    inlines = [SlideLinkInline]

class ContentNoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'display')
    
class ContentNoticeTextAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'display')

class LienKetLinkAdmin(admin.ModelAdmin):
    list_display = ['title']

class SuKienDateInline(admin.StackedInline):
    model = SuKienDate
    extra = 1

class SuKienAdmin(admin.ModelAdmin):
    list_display = ['title', 'display']
    inlines = [SuKienDateInline]
    
# Register your models here.
admin.site.register(TrangchuCategory, TrangchuCategoryAdmin)
admin.site.register(SlidePhoto, SlidePhotoAdmin)
admin.site.register(ContentNotice, ContentNoticeAdmin)
admin.site.register(ContentNoticeText, ContentNoticeTextAdmin)
admin.site.register(LienKetLink, LienKetLinkAdmin)
admin.site.register(SuKien, SuKienAdmin)