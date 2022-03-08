# Generated by Django 4.0.1 on 2022-03-08 13:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0004_alter_taggeditem_content_type_alter_taggeditem_tag'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Title')),
                ('content', models.CharField(max_length=5000, verbose_name='Content')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date creation')),
                ('drafted', models.BooleanField(default=False, verbose_name='drafted')),
                ('views', models.IntegerField(default=0, verbose_name='views')),
                ('image', models.ImageField(upload_to='')),
                ('like_count', models.IntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news', to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(related_name='liked_news', to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'ordering': ('-date_created',),
                'abstract': False,
            },
        ),
    ]
