from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation


from django.db.models.fields.related import ForeignKey
from apps.vacancy.models import Employer
from apps.base.models import Comment, AbstractPost
from taggit.managers import TaggableManager



class Event(AbstractPost):
    author = ForeignKey(settings.AUTH_USER_MODEL, related_name = "created_events", on_delete = models.CASCADE)
    organiser = ForeignKey(Employer, related_name = "events", on_delete = models.CASCADE, verbose_name="Təşkilatçı")
    starts_at = models.DateTimeField("Başlanma tarixi")
    ends_at = models.DateTimeField("Sonlanma tarixi")
    tags = TaggableManager()
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="liked_event")
    like_count = models.IntegerField(default=0)
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="in_events")
    comments = GenericRelation(Comment, related_query_name = 'event')

    def get_absolute_url(self):
        return reverse('event_detail', kwargs = {'pk': self.pk})

    def __str__(self):
        return f"[{self.title}]{self.author.user_name}"
