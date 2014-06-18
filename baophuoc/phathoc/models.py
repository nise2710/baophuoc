''' thongtin.models.py '''
from django.db import models
from ckeditor.fields import RichTextField

class PhathocCategory(models.Model):
    name = models.CharField(max_length=128,unique=True)
    tag = models.CharField(max_length=128,null=False)
    def __unicode__(self):
        return self.name

class PhathocDB(models.Model):
    category = models.ForeignKey(PhathocCategory)
    title = models.CharField(max_length=128,null=False)
    content = RichTextField()
    date = models.DateTimeField()
    display = models.BooleanField()
    url_tag = models.CharField(max_length=128,null=False)
    views = models.IntegerField(default=0,null=False)
    def __unicode__(self):
        return self.title