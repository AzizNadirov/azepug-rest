from rest_framework import serializers

from .models import Blog
from apps.base.serializers import CommentSerializer
from apps.account.serializers import MiniProfileSerializer

class BlogListSerializer(serializers.ModelSerializer):
    author = MiniProfileSerializer()
    class Meta:
        model = Blog
        fields = ['title', 'content', 'like_count', 'author']
        read_only_fields = ['views', 'author', 'like_count']



class BlogDetailSerializer(serializers.ModelSerializer):

    author = MiniProfileSerializer()
    comments = CommentSerializer(many = True)

    class Meta:
        model = Blog
        fields = ['author', 'title', 'content', 'date_created', 'like_count', 'views', 'drafted', 'comments'] 
        read_only_fields = ['date_created', 'views', 'author', 'like_count']

