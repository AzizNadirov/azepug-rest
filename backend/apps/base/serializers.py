from rest_framework import serializers

from apps.blog.models import Comment
from apps.account.serializers import MiniProfileSerializer


class CommentSerializer(serializers.ModelSerializer):
    author = MiniProfileSerializer(many = False)
    class Meta:
        model = Comment
        fields = ['content', 'like_count', 'author',]
        read_only_fields = ['author', 'like_count', ]
        



