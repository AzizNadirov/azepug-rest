from django.db import models
from django.conf import settings
from django.urls import reverse
from apps.base.models import AbstractComment, AbstractPost
from taggit.managers import TaggableManager





class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(drafted = False)
    


class Post(AbstractPost):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name= "Müəllif", related_name="posts", on_delete=models.CASCADE)
    tags = TaggableManager()
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="liked_blog")
    like_count = models.IntegerField(default=0)
    objects = models.Manager()
    published = PublishedManager()

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs = {'pk': self.pk})


    def __str__(self):
        return self.title


class Comment(AbstractComment):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name='müəllif', related_name = 'b_comments', null = True, on_delete=models.SET_NULL)
    post = models.ForeignKey(Post, related_name = 'comments', on_delete = models.CASCADE)
   
    def __str__(self):
         return f'Comment {self.author} to: {self.post}'

