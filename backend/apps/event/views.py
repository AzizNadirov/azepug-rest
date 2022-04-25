from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import permissions

from apps.base.permissions import IsOwnerOrReadOnly
from apps.base.views import increment_view

from .serializers import EventDetailSerializer, EventListSerializer
from .models import Event


class EventListAPIView(generics.ListCreateAPIView):
    serializer_class = EventListSerializer
    queryset = Event.objects.all()
    permission_classes = [IsOwnerOrReadOnly]

    def create(self, request):
        serializer = EventListSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EventDetailAPIView(APIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = EventDetailSerializer
    queryset = Event.objects.all()


    def user_is_author(self, request, user):
        return request.user == user

    def get(self, request, pk):
        event = get_object_or_404(Event, id = pk)
        serializer = EventDetailSerializer(event, many = False)
        increment_view(event, request)
        return Response(serializer.data)

    def delete(self, request, pk):
        blog = get_object_or_404(Event, id = pk)
        if self.user_is_author(request, blog.author):
            blog.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status = status.HTTP_403_FORBIDDEN)
    
    def put(self, request, pk):
        blog = get_object_or_404(Event, id = pk)
        if self.user_is_author(request, blog.author):
            serializer = EventDetailSerializer(blog, request.data, many = False)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status = status.HTTP_403_FORBIDDEN) 