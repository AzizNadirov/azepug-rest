from dataclasses import fields
from rest_framework import serializers

from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['author','body']
        



