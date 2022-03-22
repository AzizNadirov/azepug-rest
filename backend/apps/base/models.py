from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey




class AbstractPost(models.Model):
    title = models.CharField("Title", max_length = 128)
    content = models.CharField("Content", max_length = 5000)
    date_created = models.DateTimeField("Date creation",auto_now_add=True)
    drafted = models.BooleanField(verbose_name="drafted", default = False)
    viewers = models.ManyToManyField('account.Profile', blank = True, default = None)
    views = models.IntegerField(verbose_name="views", default=0)

    class Meta:
        abstract = True
        ordering = ('-date_created',)


class AbstractComment(models.Model):
    content = models.TextField('content', max_length=1024)
    date_created = models.DateTimeField("date creation", auto_now_add=True)
    like_count = models.IntegerField('like count', default = 0)

    class Meta:
        abstract = True
        ordering = ('-date_created',)