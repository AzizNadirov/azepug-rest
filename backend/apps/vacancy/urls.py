from django.urls import path

from .views import VacancyListAPIView, VacancyDetailAPIView, ListCreateEmployerView


urlpatterns = [
    path('', VacancyListAPIView.as_view(), name = 'list-vacancy'),
    path('<int:pk>', VacancyDetailAPIView.as_view(), name = 'detail-vacancy'),
    path('add_emp', ListCreateEmployerView.as_view(), name = 'create-employer'),
]