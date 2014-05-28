''' thongtin.models.py '''
from django.db import models
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=128,unique=True)
    
    def __unicode__(self):
        return self.name

class Content(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128,null=False)
    content = RichTextField()
    date = models.DateTimeField()
    display = models.BooleanField()
    url_tag = models.CharField(max_length=128,null=False)
    
    def __unicode__(self):
        return self.title