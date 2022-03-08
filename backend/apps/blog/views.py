from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import permissions

from .serializers import BlogSerializer
from .models import Blog, Comment


class BlogListAPIView(generics.ListCreateAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.published.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BlogDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = BlogSerializer
    queryset = Blog.published.all()

    def user_is_author(self, request, user):
        return request.user == user

    def get(self, request, pk):
        blog = get_object_or_404(Blog, id = pk)
        serializer = BlogSerializer(blog, many = False)
        return Response(serializer.data)

    def delete(self, request, pk):
        blog = get_object_or_404(Blog, id = pk)
        if self.user_is_author(request, blog.author):
            blog.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status = status.HTTP_403_FORBIDDEN)
    
    def put(self, request, pk):
        blog = get_object_or_404(Blog, id = pk)
        if self.user_is_author(request, blog.author):
            serializer = BlogSerializer(blog, request.data, many = False)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status = status.HTTP_403_FORBIDDEN) 

