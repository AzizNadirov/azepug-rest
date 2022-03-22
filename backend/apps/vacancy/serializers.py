from rest_framework import serializers

from .models import Vacancy, Employer
from apps.base.serializers import CommentSerializer
from apps.account.serializers import MiniProfileSerializer




class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = '__all__'


class VacancyListSerializer(serializers.ModelSerializer):
    author = MiniProfileSerializer()
    employer = EmployerSerializer()
    class Meta:
        model = Vacancy
        exclude = ['views', 'likes', 'like_count', 'date_created']


class VacancyDetailSerializer(serializers.ModelSerializer):
    author = MiniProfileSerializer()
    employer = EmployerSerializer()
    comments = CommentSerializer(many = True)

    class Meta:
        model = Vacancy
        fields = ['author', 'title', 'content', 'date_created','employer','dead_line','freelance' ,
            'min_salary', 'contact','like_count', 'views', 'drafted', 'comments'] 
        read_only_fields = ['date_created', 'views', 'author', 'like_count']