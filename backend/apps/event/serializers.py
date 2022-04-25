from rest_framework import serializers

from django.apps import apps

from .models import Event
from apps.base.serializers import CommentSerializer
from apps.account.serializers import MiniProfileSerializer
from apps.vacancy.serializers import EmployerSerializer



class EventListSerializer(serializers.ModelSerializer):

    author = MiniProfileSerializer(default=serializers.CurrentUserDefault())
    organiser = EmployerSerializer()


    def create(self, validated_data):
        print('%'*50, validated_data)
        Event = apps.get_model('event', 'Event')
        Employer = apps.get_model('vacancy', 'Employer')
        employer = Employer.objects.get(pk = validated_data['organiser'])
        author = self.context['request'].user
        instance = Event.objects.create( author = author, 
                                        title = validated_data['title'],
                                        content = validated_data['content'],
                                        starts_at = validated_data['starts_at'],
                                        ends_at = validated_data['ends_at'],
                                        organiser = employer)
        return instance

    class Meta:
        model = Event
        fields = ['title', 'content', 'like_count', 'author', 'starts_at', 'ends_at', 'organiser']

class EventDetailSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many = True)
    author = MiniProfileSerializer(default=serializers.CurrentUserDefault())

    class Meta:
        model = Event
        fields = ['author' ,'title', 'content', 'date_created', 'like_count', 'views', 'drafted', 'comments'] 
        read_only_fields = ['date_created', 'views', 'author', 'like_count']
