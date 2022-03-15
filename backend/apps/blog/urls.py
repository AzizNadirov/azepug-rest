from django.urls import path

from .views import BlogListAPIView, BlogDetailAPIView


urlpatterns = [
    path('', BlogListAPIView.as_view(), name = 'list-blog'),
    path('<int:pk>', BlogDetailAPIView.as_view(), name = 'detail-blog'),
]