from rest_framework import serializers

from .models import Blog
from apps.base.serializers import CommentSerializer



class BlogSerializer(serializers.ModelSerializer):
    comments = CommentSerializer()
    class Meta:
        model = Blog
        exclude = ['views', 'likes', 'like_count', 'date_created']

