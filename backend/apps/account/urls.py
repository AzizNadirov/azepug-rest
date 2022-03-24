from django.urls import path
from .views import DetailUpdateDestroyUserAPI


urlpatterns = [
    path('<str:user_name>', DetailUpdateDestroyUserAPI.as_view(), name = 'detail_user'),

]
