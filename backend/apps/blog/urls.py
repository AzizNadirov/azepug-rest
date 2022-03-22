from django.urls import path

from apps.base.views import LikeView, SaveView, SupportView

from .views import BlogListAPIView, BlogDetailAPIView



urlpatterns = [
    path('', BlogListAPIView.as_view(), name = 'list-blog'),
    path('<int:pk>', BlogDetailAPIView.as_view(), name = 'detail-blog'),
    path('<int:pk>/like', LikeView.as_view(), name = 'like-blog'),
    path('<int:pk>/save', SaveView.as_view(), name = 'save-blog'),
]