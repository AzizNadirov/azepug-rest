from django.db import models
from django.urls import reverse
from django.conf import settings

from apps.vacancy.models import Employer
from apps.base.models import AbstractPost, AbstractComment
from taggit.managers import TaggableManager



class Event(AbstractPost):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = "created_events", on_delete = models.CASCADE)
    organiser = models.ForeignKey(Employer, related_name = "events", on_delete = models.CASCADE, verbose_name="Təşkilatçı")
    starts_at = models.DateTimeField("Başlanma tarixi")
    ends_at = models.DateTimeField("Sonlanma tarixi")
    tags = TaggableManager()
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="liked_event")
    like_count = models.IntegerField(default=0)
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="in_events", blank = True)
    comments = models.ForeignKey('event.Comment', related_name='for_events', on_delete = models.DO_NOTHING, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('event_detail', kwargs = {'pk': self.pk})

    def __str__(self):
        return  f'<event: {self.title} - {self.author}>'


class Comment(AbstractComment):
    author = models.ForeignKey('account.Profile', related_name='event_comments', on_delete = models.SET_NULL, null=True, blank=True)
    likers = models.ManyToManyField('account.Profile', related_name='liked_event_comments', blank=True)
