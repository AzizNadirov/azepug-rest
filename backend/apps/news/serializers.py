from django.shortcuts import get_object_or_404
from rest_framework import serializers

from .models import News
from apps.base.serializers import CommentSerializer
from apps.account.serializers import MiniProfileSerializer
from apps.base.views import get_models



class NewsListSerializer(serializers.ModelSerializer):
    author = MiniProfileSerializer()

    # def create(self, validated_data):
    #     Profile = get_models()['profile']
    #     author = validated_data.pop('author')
    #     author = get_object_or_404(Profile, user_name = author['user_name'])
    #     news = News.objects.create(author = author, **validated_data)
    #     return news

    class Meta:
        model = News
        fields = ['title', 'content', 'like_count', 'author']
        read_only_fields = ['views', 'author', 'like_count']


class NewsDetailSerializer(serializers.ModelSerializer):
    author = MiniProfileSerializer(write_only = True, default=serializers.CurrentUserDefault())
    comments = CommentSerializer(many = True)

    class Meta:
        model = News
        fields = ['author', 'title', 'content', 'date_created', 'like_count', 'views', 'drafted', 'comments']
        read_only_fields = ['date_created', 'views', 'author', 'like_count']
