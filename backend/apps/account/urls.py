from django.urls import path, include
from .views import DetailUserApi


urlpatterns = [
    path('<str:user_name>', DetailUserApi.as_view(), name = 'detail_user'),

]
