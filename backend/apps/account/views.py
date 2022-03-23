from django.shortcuts import render, get_object_or_404
from django.apps import apps

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .serializers import RegisterUserSerializer, ProfileSerializer

from apps.blog.serializers import BlogListSerializer
from apps.event.serializers import EventListSerializer
from apps.news.serializers import NewsListSerializer
from apps.vacancy.serializers import VacancyListSerializer
from apps.forum.serializers import QuestionListSerializer, AnswerListSerializer



def collect_user_recents(user, num_recents = 5):
    blogs = BlogListSerializer(apps.get_model('blog', 'Blog').published.filter(author = user).order_by('date_created'), many = True)
    events = EventListSerializer(apps.get_model('event', 'Event').published.filter(author = user).order_by('date_created'), many = True)
    news = NewsListSerializer(apps.get_model('news', 'News').published.filter(author = user).order_by('date_created'), many = True)
    vacancies = VacancyListSerializer(apps.get_model('vacancy', 'Vacancy').published.filter(author = user).order_by('date_created'), many = True)
    questions = QuestionListSerializer(apps.get_model('forum', 'Question').published.filter(author = user).order_by('date_created'), many = True)
    answers = AnswerListSerializer(apps.get_model('forum', 'Answer').published.filter(author = user).order_by('date_created'), many = True)
    data = {'blogs': blogs.data, 'events': events.data, 'news': events.data, 'news': news.data,
     'vacancies': vacancies.data, 'questions': questions.data, 'answers': answers.data }

    return data

class AccountCreateView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        reg_serializer = RegisterUserSerializer(data = request.data)
        if reg_serializer.is_valid():
            new_user = reg_serializer.save()
            if new_user:
                return Response(status=status.HTTP_201_CREATED)
        return Response(reg_serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class DetailUserApi(APIView):
    Profile = apps.get_model('account', 'Profile')
    queryset = Profile.objects.all()
    def get(self, request, user_name):
        user = get_object_or_404(self.Profile, user_name = user_name)
        profile = ProfileSerializer(user).data
        recents = collect_user_recents(user)
        data = {'profile': profile, 'recents': recents}
        return Response(data=data, status=status.HTTP_200_OK)

