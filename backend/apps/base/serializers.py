from rest_framework import serializers

from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['content_type' ,'author','body', 'created_at']
        



