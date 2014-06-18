from django.db import models
from ckeditor.fields import RichTextField

class TrangchuCategory(models.Model):
    name = models.CharField(max_length=128,unique=True)
    tag = models.CharField(max_length=128,null=False)
    def __unicode__(self):
        return self.name
    
class SlidePhoto(models.Model):
    category = models.ForeignKey(TrangchuCategory)
    title = models.CharField(max_length=128,null=False)
    author = models.CharField(max_length=128,null=True)
    date = models.DateTimeField()
    display = models.BooleanField()
    url_tag = models.CharField(max_length=128,null=False)
    views = models.IntegerField(default=0,null=False)
    
class SlideLink(models.Model):
    content_photo = models.ForeignKey(SlidePhoto)
    title = models.CharField(max_length=255,null=False)
    url = models.URLField(max_length=255)

class ContentNoticeText(models.Model):
    title = models.CharField(max_length=128,null=False)
    content = RichTextField()
    date = models.DateTimeField()
    display = models.BooleanField()
    def __unicode__(self):
        return self.title
    
class ContentNotice(models.Model):
    title = models.CharField(max_length=128,null=False)
    page_url = models.URLField(max_length=255)
    date = models.DateTimeField()
    display = models.BooleanField()
    def __unicode__(self):
        return self.title

class LienKetLink(models.Model):
    title = models.CharField(max_length=128,null=False)
    link = models.URLField(max_length=255)
    def __unicode__(self):
        return self.title

class SuKien(models.Model):
    title = models.CharField(max_length=128,null=False)
    display = models.BooleanField()
    
class SuKienDate(models.Model):
    content_sukien = models.ForeignKey(SuKien)
    event_title = models.CharField(max_length=128,null=False)
    date = models.DateTimeField(null=False)