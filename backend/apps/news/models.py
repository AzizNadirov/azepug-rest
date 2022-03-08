from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation


from django.urls.base import reverse
from taggit.managers import TaggableManager
from apps.base.models import AbstractPost, Comment


class News(AbstractPost):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = "news")
    image = models.ImageField()
    tags = TaggableManager()
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="liked_news")
    like_count = models.IntegerField(default=0)
    comments = GenericRelation(Comment, related_query_name = 'news')

    def __str__(self):
        return f"News: {self.title} : {self.author}"
    
    def get_absolute_url(self):
        return reverse("news_detail", kwargs={"pk": self.pk})
