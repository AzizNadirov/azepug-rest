# Generated by Django 4.0.1 on 2022-03-23 12:38

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy', '0004_comment_vacancy_comments'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='vacancy',
            managers=[
                ('published', django.db.models.manager.Manager()),
            ],
        ),
    ]
