from django.urls import path

from .views import EventListAPIView, EventDetailAPIView


urlpatterns = [
    path('', EventListAPIView.as_view(), name = 'list-event'),
    path('<int:pk>', EventDetailAPIView.as_view(), name = 'detail-event'),
]