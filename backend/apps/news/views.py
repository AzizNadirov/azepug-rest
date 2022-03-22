from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import permissions

from apps.base.permissions import IsOwnerOrReadOnly
from apps.base.views import increment_view


from .serializers import NewsDetailSerializer, NewsListSerializer
from .models import News


class NewsListAPIView(generics.ListCreateAPIView):
    serializer_class = NewsListSerializer
    queryset = News.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class NewsDetailAPIView(APIView):
    permission_classes = [IsOwnerOrReadOnly]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = NewsDetailSerializer
    queryset = News.objects.all()

    class Meta:
        extra_kwargs = {'like_count':{"read_only":True}, 'views': {'read_only': True}}

    def user_is_author(self, request, user):
        return request.user == user

    def get(self, request, pk):
        news = get_object_or_404(News, id = pk)
        serializer = NewsDetailSerializer(news, many = False)
        increment_view(news, request)
        return Response(serializer.data)

    def delete(self, request, pk):
        blog = get_object_or_404(News, id = pk)
        if self.user_is_author(request, blog.author):
            blog.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status = status.HTTP_403_FORBIDDEN)
    
    def put(self, request, pk):
        blog = get_object_or_404(News, id = pk)
        if self.user_is_author(request, blog.author):
            serializer = NewsDetailSerializer(blog, request.data, many = False)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status = status.HTTP_403_FORBIDDEN) 

