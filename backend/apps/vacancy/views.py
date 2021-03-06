from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import permissions

from apps.base.permissions import IsOwnerOrReadOnly
from apps.base.views import increment_view

from .serializers import VacancyDetailSerializer, VacancyListSerializer, EmployerSerializer
from .models import Vacancy, Employer



class ListCreateEmployerView(generics.ListCreateAPIView):
    serializer_class = EmployerSerializer
    queryset = Employer.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request):
        serializer = EmployerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(data = serializer.errors)


class VacancyListAPIView(generics.ListCreateAPIView):
    serializer_class = VacancyListSerializer
    queryset = Vacancy.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class VacancyDetailAPIView(APIView):
    permission_classes = [IsOwnerOrReadOnly]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = VacancyDetailSerializer
    queryset = Vacancy.objects.all()

    class Meta:
        extra_kwargs = {'like_count':{"read_only":True}, 'views': {'read_only': True}}

    def user_is_author(self, request, user):
        return request.user == user

    def get(self, request, pk):
        vacancy = get_object_or_404(Vacancy, id = pk)
        serializer = VacancyDetailSerializer(vacancy, many = False)
        increment_view(vacancy, request)
        return Response(serializer.data)

    def delete(self, request, pk):
        vacancy = get_object_or_404(Vacancy, id = pk)
        if self.user_is_author(request, vacancy.author):
            vacancy.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status = status.HTTP_403_FORBIDDEN)
    
    def put(self, request, pk):
        vacancy = get_object_or_404(Vacancy, id = pk)
        if self.user_is_author(request, vacancy.author):
            serializer = VacancyDetailSerializer(vacancy, request.data, many = False)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status = status.HTTP_403_FORBIDDEN) 

