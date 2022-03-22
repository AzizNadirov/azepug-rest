from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import permissions

from apps.base.permissions import IsOwnerOrReadOnly
from apps.base.views import increment_view

from .serializers import AnswerDetailSerializer, QuestionListSerializer, QuestionDetailSerializer
from .models import Answer, Question


class QuestionListAPIView(generics.ListCreateAPIView):
    serializer_class = QuestionListSerializer
    queryset = Question.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author = self.request.user)


class QuestionDetailAPIView(APIView):
    permission_classes = [IsOwnerOrReadOnly]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = QuestionDetailSerializer
    queryset = Question.objects.all()

    def user_is_author(self, request, user):
        return request.user == user

    def get(self, request, pk):
        question = get_object_or_404(Question, id = pk)
        serializer = QuestionDetailSerializer(question, many = False)
        increment_view(question, request)
        return Response(serializer.data)

    def delete(self, request, pk):
        question = get_object_or_404(Question, id = pk)
        if self.user_is_author(request, question.author):
            question.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status = status.HTTP_403_FORBIDDEN)
    
    def put(self, request, pk):
        question = get_object_or_404(Question, id = pk)
        if self.user_is_author(request, question.author):
            serializer = AnswerDetailSerializer(question, request.data, many = False)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status = status.HTTP_403_FORBIDDEN) 


class AnswerDetailAPIView(APIView):
    permission_classes = [IsOwnerOrReadOnly]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def user_is_author(self, request, user):
        return request.user == user

    def get(self, request, q_pk, a_pk):
        question = get_object_or_404(Question, pk = q_pk)
        answer = get_object_or_404(question.answers.all(), pk = a_pk)
        serializer = AnswerDetailSerializer(answer, many = False)
        increment_view(answer)
        return Response(serializer.data)

    def delete(self, request, q_pk, a_pk):
        answer = get_object_or_404(Answer, id = a_pk)
        if self.user_is_author(request, answer.author):
            answer.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status = status.HTTP_403_FORBIDDEN)
    
    def put(self, request, q_pk ,a_pk):
        answer = get_object_or_404(Answer, id = a_pk)
        if self.user_is_author(request, Question.author):
            serializer = AnswerDetailSerializer(answer, request.data, many = False)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status = status.HTTP_403_FORBIDDEN) 