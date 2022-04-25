from rest_framework import serializers

from django.apps import apps
from .models import Blog
from apps.base.serializers import CommentSerializer
from apps.account.serializers import MiniProfileSerializer




class BlogListSerializer(serializers.ModelSerializer):
    author = MiniProfileSerializer(default=serializers.CurrentUserDefault())
    def create(self, validated_data):
        Profile = apps.get_model('account', 'Profile')
        Blog = apps.get_model('blog', 'Blog')
        author = self.context['request'].user
        instance = Blog.objects.create( author = author, 
                                        title = validated_data['title'],
                                        content = validated_data['content'])
        return instance

    class Meta:
        model = Blog
        fields = ['id', 'title', 'content', 'like_count', 'author']
        read_only_fields = ['views', 'author', 'like_count']



class BlogDetailSerializer(serializers.ModelSerializer):

    author = MiniProfileSerializer(read_only=True)
    comments = CommentSerializer(many = True)


    class Meta:
        model = Blog
        fields = ['author', 'title', 'content', 'date_created', 'like_count', 'views', 'drafted', 'comments'] 
        read_only_fields = ['date_created', 'views', 'author', 'like_count']

