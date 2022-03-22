from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from PIL import Image
import os
from django.db.models.signals import post_save

from django.urls.base import reverse
from core.settings import MEDIA_ROOT

# from apps.event.models import Event
# from apps.blog.models import Blog
# from apps.news.models import News
# from apps.forum.models import Question
# from apps.vacancy.models import Vacancy


def photo_upload(instance, filename):
    dir = os.path.join(MEDIA_ROOT,'profile_images',f'{instance.user_name}' )
    walk = list(os.walk(dir))
    try:
        for old_photo in walk[-1][-1]:
            os.remove(os.path.join(dir,old_photo))
    except: IndexError
    return f'profile_images/{instance.user_name}/{filename}'


class Contacts(models.Model):
    email = models.EmailField(null = True)
    github = models.URLField(null = True)
    linkedin = models.URLField(null = True)
    phone = models.CharField(null = True, max_length=20)



class ProfileManager(BaseUserManager):

    def create_superuser(self, email, user_name, first_name, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)
        return self.create_user(email, user_name, first_name, password, **kwargs)

    def create_user(self, email, user_name, first_name, password, **kwargs):
        email = self.normalize_email(email)
        user = self.model(email = email, user_name=user_name, first_name = first_name, **kwargs)
        user.set_password(password)
        ## do some validations
        user.save()
        return user


class Profile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    user_name = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    start_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to=photo_upload, default = 'profile_pics/default_avatar.jpg',
            null=True, blank = True)
    about = models.TextField(max_length=1024, blank = True, null = True)
    contacts = models.ManyToManyField(Contacts, related_name='profiles')
    is_staff = models.BooleanField(default = True)
    is_active = models.BooleanField(default = True)
    objects = ProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name']

    objects = ProfileManager()
    
    def get_absolute_url(self):
        return reverse('user', kwargs = {'pk': self.pk})
    
    def __str__(self):
        return f'{self.user_name}' 


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.image:
            self.image = f"{os.path.join(MEDIA_ROOT, 'profile_pics')}/default_avatar.jpg"
        else:
            img = Image.open(self.image.path)
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.image.path)


class Treasure(models.Model):
    profile = models.OneToOneField(Profile, on_delete = models.CASCADE, related_name='treasure')
    blog = models.ManyToManyField('blog.Blog', related_name = 'treasure')
    event = models.ManyToManyField('event.Event', related_name = 'treasure')
    news = models.ManyToManyField('news.News', related_name = 'treasure')
    question = models.ManyToManyField('forum.Question', related_name = 'treasure')
    vacancy = models.ManyToManyField('vacancy.Vacancy', related_name = 'treasure')

    def __str__(self):
        return f"{self.profile.user_name}'s Treasure"


def create_treasure(sender, instance, created, **kwargs):
    if created:
        Treasure.objects.create(profile = instance)

post_save.connect(create_treasure, sender = Profile)