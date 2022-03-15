from dataclasses import fields
from rest_framework import serializers

from .models import Blog
from apps.base.serializers import CommentSerializer
from apps.account.serializers import MiniProfileSerializer



class BlogListSerializer(serializers.ModelSerializer):
    author = MiniProfileSerializer()
    class Meta:
        model = Blog
        exclude = ['views', 'likes', 'like_count', 'date_created']


class BlogDetailSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    # comments = serializers.SerializerMethodField()
    comments = CommentSerializer(many = True)

    class Meta:
        model = Blog
        fields = ['author', 'title', 'content', 'date_created', 'like_count', 'views', 'drafted', 'comments'] 

    def get_author(self, obj):
        return str(obj.author)
