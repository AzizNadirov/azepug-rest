from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation

from django.urls import reverse
from apps.base.models import AbstractPost, Comment
from taggit.managers import TaggableManager





class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(drafted = False)
    


class Blog(AbstractPost):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name= "Müəllif", related_name="blogs", on_delete=models.CASCADE)
    tags = TaggableManager()
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="liked_blog")
    like_count = models.IntegerField(default=0)
    objects = models.Manager()
    published = PublishedManager()
    comments = GenericRelation(Comment, related_query_name = 'blogs')

    def get_absolute_url(self):
        return reverse('detail-blog', kwargs = {'pk': self.pk})


    def __str__(self):
        return self.title



