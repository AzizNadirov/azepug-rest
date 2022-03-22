from django.urls import path

from .views import EventListAPIView, EventDetailAPIView
from apps.base.views import LikeView, SaveView


urlpatterns = [
    path('', EventListAPIView.as_view(), name = 'list-event'),
    path('<int:pk>', EventDetailAPIView.as_view(), name = 'detail-event'),
    path('<int:pk>/like', LikeView.as_view(), name = 'like-event'),
    path('<int:pk>/save', SaveView.as_view(), name = 'save-event'),
]