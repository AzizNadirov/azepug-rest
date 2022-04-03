from django.urls import path

from apps.base.views import LikeView, SaveView

from .views import BlogListAPIView, BlogDetailAPIView



urlpatterns = [
    path('', BlogListAPIView.as_view(), name = 'blog-list'),
    path('<int:pk>', BlogDetailAPIView.as_view(), name = 'blog-detail'),
    path('<int:pk>/like', LikeView.as_view(), name = 'like-blog'),
    path('<int:pk>/save', SaveView.as_view(), name = 'save-blog'),
]