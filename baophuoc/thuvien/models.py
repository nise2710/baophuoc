from django.db import models

class ThuvienCategory(models.Model):
    name = models.CharField(max_length=128,unique=True)
    tag = models.CharField(max_length=128,null=False)
    def __unicode__(self):
        return self.name

class ContentVideo(models.Model):
    category = models.ForeignKey(ThuvienCategory)
    title = models.CharField(max_length=128,null=False)
    url = models.URLField(max_length=255)
    author = models.CharField(max_length=128,null=True)
    date = models.DateTimeField()
    display = models.BooleanField()
    url_tag = models.CharField(max_length=128,null=False)
    views = models.IntegerField(default=0,null=False)

class ContentPhoto(models.Model):
    category = models.ForeignKey(ThuvienCategory)
    title = models.CharField(max_length=128,null=False)
    author = models.CharField(max_length=128,null=True)
    thumbnail = models.URLField(max_length=255,null=True)
    date = models.DateTimeField()
    display = models.BooleanField()
    url_tag = models.CharField(max_length=128,null=False)
    views = models.IntegerField(default=0,null=False)
    
class ContentPhotoLink(models.Model):
    content_photo = models.ForeignKey(ContentPhoto)
    title = models.CharField(max_length=255,null=False)
    url = models.URLField(max_length=255)