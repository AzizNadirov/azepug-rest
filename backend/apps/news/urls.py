from django.urls import path

from apps.base.views import LikeView, SaveView

from .views import NewsListAPIView, NewsDetailAPIView


urlpatterns = [
    path('', NewsListAPIView.as_view(), name = 'list-news'),
    path('<int:pk>', NewsDetailAPIView.as_view(), name = 'detail-news'),
    path('<int:pk>/like', LikeView.as_view(), name = 'like-blog'),
    path('<int:pk>/save', SaveView.as_view(), name = 'save-blog'),
]