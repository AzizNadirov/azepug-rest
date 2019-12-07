from django.db import models
from django.conf import settings

from django.urls.base import reverse
from taggit.managers import TaggableManager
from apps.base.models import AbstractPost, AbstractComment


class News(AbstractPost):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = "newss")
    image = models.ImageField(blank = True)
    tags = TaggableManager()
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="liked_news", blank = True)
    like_count = models.IntegerField(default=0)
    comments = models.ForeignKey('news.Comment', related_name='for_news', on_delete = models.DO_NOTHING, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'News'


    def __str__(self):
        return f'<news: {self.title} - {self.author}>'
    
    def get_absolute_url(self):
        return reverse("news_detail", kwargs={"pk": self.pk})


class Comment(AbstractComment):
    author = models.ForeignKey('account.Profile', related_name='news_comments', on_delete = models.SET_NULL, null=True, blank=True)
    likers = models.ManyToManyField('account.Profile', related_name='liked_news_comments', blank=True)