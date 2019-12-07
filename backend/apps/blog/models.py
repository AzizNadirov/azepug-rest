from django.db import models
from django.conf import settings
from django.urls import reverse

from apps.base.models import AbstractPost, AbstractComment
from taggit.managers import TaggableManager
from apps.base.models import AbstractComment



class Blog(AbstractPost):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name= "Müəllif", related_name="blogs", on_delete=models.CASCADE)
    tags = TaggableManager()
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="liked_blog")
    like_count = models.IntegerField(default=0)
    comments = models.ForeignKey('blog.Comment', related_name='for_blogs', on_delete = models.DO_NOTHING, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('detail-blog', kwargs = {'pk': self.pk})


    def __str__(self):
        return f'<blog: test_title - {self.author}>'


class Comment(AbstractComment):
    author = models.ForeignKey('account.Profile', related_name='blog_comments', on_delete = models.SET_NULL, null=True, blank=True)
    likers = models.ManyToManyField('account.Profile', related_name='liked_blog_comments', blank=True)

