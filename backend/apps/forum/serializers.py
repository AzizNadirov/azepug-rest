from email.policy import default
from rest_framework import serializers

from .models import Question, Answer
from apps.base.serializers import CommentSerializer
from apps.account.serializers import MiniProfileSerializer



class QuestionListSerializer(serializers.ModelSerializer):
    author = MiniProfileSerializer()
    class Meta:
        model = Question
        fields = ['author', 'title', 'content', 'date_created', 'views', 'supports_count', 'drafted', 'closed'] 
        read_only_fields = ['date_created', 'views', 'supports_count', 'closed', 'author']



class AnswerListSerializer(serializers.ModelSerializer):
    author = MiniProfileSerializer()
        
    class Meta:
        model = Answer
        fields = ['author', 'content', 'date_created', 'views', 'supports_count', 'drafted'] 


class QuestionDetailSerializerMini(serializers.ModelSerializer):
    """ Serializes only author, title and content """
    author = MiniProfileSerializer()

    class Meta:
        model = Question
        fields = ['author', 'title', 'content'] 
    
class QuestionDetailSerializer(serializers.ModelSerializer):
    author = MiniProfileSerializer()
    answers = AnswerListSerializer(many = True)

    class Meta:
        model = Question
        fields = ['author', 'title', 'content', 'date_created', 'views', 'supports_count', 'drafted', 'closed', 'answers']


class AnswerDetailSerializer(serializers.ModelSerializer):
    author = MiniProfileSerializer()
    question = QuestionDetailSerializerMini()
    # comments = CommentSerializer(many = True)

    class Meta:
        model = Answer
        fields = ['question', 'author', 'content', 'date_created', 'views', 'supports_count', 'drafted'] 