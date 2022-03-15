from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import permissions

from apps.base.permissions import IsOwnerOrReadOnly

from .serializers import EventDetailSerializer, EventListSerializer
from .models import Event


class EventListAPIView(generics.ListCreateAPIView):
    serializer_class = EventListSerializer
    queryset = Event.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class EventDetailAPIView(APIView):
    # permission_classes = [IsOwnerOrReadOnly]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = EventDetailSerializer
    queryset = Event.objects.all()

    class Meta:
        extra_kwargs = {'like_count':{"read_only":True}, 'views': {'read_only': True}}

    def user_is_author(self, request, user):
        return request.user == user

    def get(self, request, pk):
        event = get_object_or_404(Event, id = pk)
        serializer = EventDetailSerializer(event, many = False)
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

