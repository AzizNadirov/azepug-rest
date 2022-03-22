from rest_framework import serializers

from .models import News
from apps.base.serializers import CommentSerializer
from apps.account.serializers import MiniProfileSerializer



class NewsListSerializer(serializers.ModelSerializer):
    author = MiniProfileSerializer()
    class Meta:
        model = News
        exclude = ['views', 'likes', 'like_count', 'date_created']
        read_only_fields = ['date_created', 'views', 'author', 'like_count']

class NewsDetailSerializer(serializers.ModelSerializer):
    author = MiniProfileSerializer()
    comments = CommentSerializer(many = True)

    class Meta:
        model = News
        fields = ['author', 'title', 'content', 'date_created', 'like_count', 'views', 'drafted', 'comments']
        read_only_fields = ['date_created', 'views', 'author', 'like_count']
