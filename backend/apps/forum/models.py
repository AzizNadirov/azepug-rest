from django.db import models
from django.urls import reverse
from django.conf import settings
from taggit.managers import TaggableManager


from apps.base.models import AbstractComment, AbstractPost


class Comment(AbstractComment):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='müəllif', related_name = 'f_comments', 
        null = True, on_delete=models.SET_NULL)
    answer = models.ForeignKey('Answer', related_name = 'comments', on_delete = models.CASCADE)

    def __str__(self):
         return f'Comment {self.author} to answer: {self.answer}'


class Question(AbstractPost):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="questions")
    supports = models.ManyToManyField(to = 'account.Profile', related_name = "supported_question")
    supports_count = models.IntegerField(default=0)
    last_edited = models.DateTimeField(auto_now = True)
    tags = TaggableManager()
    closed = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.title[:51]} : {self.author.user_name}"


    def get_absolute_url(self):
        return reverse('question_detail', kwargs = {'pk': self.id})



class Answer(AbstractPost):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="answers")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name= "answers")
    supports = models.ManyToManyField(to = 'account.Profile', related_name = "supported_answer")
    supports_count = models.IntegerField(default=0)
    last_edited = models.DateTimeField(auto_now = True)
    title = None

    def __str__(self):
        return f"Answer {self.author} to {self.question.title}"

    def get_absolute_url(self):
        return reverse('answer_detail', kwargs = {'pk':self.question.id,'a_pk': self.pk})
