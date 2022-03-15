from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey




class AbstractPost(models.Model):
    title = models.CharField("Title", max_length = 128)
    content = models.CharField("Content", max_length = 5000)
    date_created = models.DateTimeField("Date creation",auto_now_add=True)
    drafted = models.BooleanField(verbose_name="drafted", default = False)
    views = models.IntegerField(verbose_name="views", default=0)

    class Meta:
        abstract = True
        ordering = ('-date_created',)

 
    
class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name='müəllif', related_name = 'b_comments', null = True, on_delete=models.SET_NULL)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    body = models.TextField()
    created_at = models.DateTimeField('Yaradılma tarixi',auto_now_add = True)
    updated = models.DateTimeField('Yenilənmə tariix', auto_now = True)
    active = models.BooleanField('Aktiv', default = True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
         return f'Comment {self.author} to: {self.content_type}'