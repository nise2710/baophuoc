''' thongtin.models.py '''
from django.db import models
from ckeditor.fields import RichTextField

class ThongtinCategory(models.Model):
    name = models.CharField(max_length=128,unique=True)
    tag = models.CharField(max_length=128,null=False)
    def __unicode__(self):
        return self.name

class ThongtinDB(models.Model):
    category = models.ForeignKey(ThongtinCategory)
    title = models.CharField(max_length=128,null=False)
    content = RichTextField()
    thumbnail = models.URLField(max_length=255,null=True)
    date = models.DateTimeField()
    news_display = models.BooleanField()
    display = models.BooleanField()
    url_tag = models.CharField(max_length=128,null=False)
    views = models.IntegerField(default=0,null=False)
    def __unicode__(self):
        return self.title