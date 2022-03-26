# Generated by Django 4.0.1 on 2022-03-24 13:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0003_initial'),
        ('news', '0001_initial'),
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='treasure',
            name='news',
            field=models.ManyToManyField(related_name='treasure', to='news.News'),
        ),
        migrations.AddField(
            model_name='treasure',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='treasure', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='treasure',
            name='question',
            field=models.ManyToManyField(related_name='treasure', to='forum.Question'),
        ),
    ]
