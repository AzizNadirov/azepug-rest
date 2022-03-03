from django.db import models
from django.utils import timezone




class AbstractPost(models.Model):
    title = models.CharField("Title", max_length = 128)
    content = models.CharField("Content", max_length = 5000)
    date_created = models.DateTimeField("Date creation", default= timezone.now)
    drafted = models.BooleanField(verbose_name="drafted", default = False)
    views = models.IntegerField(verbose_name="views", default=0)

    class Meta:
        abstract = True
        ordering = ('-date_created',)



class AbstractComment(models.Model):
    body = models.TextField('Şərh')
    created_at = models.DateTimeField('Yaradılma tarixi',auto_now_add = True)
    updated = models.DateTimeField('Yenilənmə tariix', auto_now = True)
    active = models.BooleanField('Aktiv', default = True)

    class Meta:
        abstract = True
        ordering = ('-created_at',)

