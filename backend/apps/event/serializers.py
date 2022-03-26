from rest_framework import serializers

from .models import Event
from apps.base.serializers import CommentSerializer
from apps.account.serializers import MiniProfileSerializer



class EventListSerializer(serializers.ModelSerializer):
    author = MiniProfileSerializer()

    class Meta:
        model = Event
        fields = ['title', 'content', 'like_count', 'author']

class EventDetailSerializer(serializers.ModelSerializer):
    author = MiniProfileSerializer()
    comments = CommentSerializer(many = True)

    class Meta:
        model = Event
        fields = ['author' ,'title', 'content', 'date_created', 'like_count', 'views', 'drafted', 'comments'] 
        read_only_fields = ['date_created', 'views', 'author', 'like_count']

