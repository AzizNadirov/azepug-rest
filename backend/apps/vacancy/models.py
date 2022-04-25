from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from django.urls import reverse

from taggit.managers import TaggableManager
from apps.base.models import AbstractPost, AbstractComment



class Employer(models.Model):
    name = models.CharField( "Name" ,max_length=128)
    workers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = "works_at", verbose_name = "workers", blank = True)
    founded_at = models.DateField("Date created", null = True, blank = True)


    def __str__(self):
        return f'<employer: emp name - {self.added_by}>'


class Vacancy(AbstractPost):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='vacancies', on_delete=models.CASCADE)
    employer = models.ForeignKey(Employer, related_name = 'vacancies', on_delete=models.CASCADE)
    dead_line = models.DateField("Date expiration (YYYY-MM-DD)", null=True)
    freelance = models.BooleanField("Remote")
    contact = models.CharField( "Contact" ,max_length=128)
    min_salary = models.PositiveIntegerField("Min salary")
    tags = TaggableManager()
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="liked_vacancy")
    like_count = models.IntegerField(default=0)
    comments = models.ForeignKey('vacancy.Comment', related_name='for_vacancies', on_delete = models.DO_NOTHING, blank=True, null=True)


    def get_absolute_url(self):
        return reverse('vacancy_detail', kwargs = {'pk': self.pk})

    class Meta:
        verbose_name = 'vacancy'
        verbose_name_plural = 'vacancies'
    def __str__(self):
        return f'<vacancy: {self.title} - {self.author}>'


class Comment(AbstractComment):
    author = models.ForeignKey('account.Profile', related_name='vacancy_comments', on_delete = models.SET_NULL, null=True, blank=True)
    likers = models.ManyToManyField('account.Profile', related_name='liked_vacancy_comments', blank=True)