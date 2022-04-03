from django.urls import path

from .views import AnswerDetailAPIView, QuestionListAPIView, QuestionDetailAPIView

from apps.base.views import SaveView, SupportView

urlpatterns = [
    path('', QuestionListAPIView.as_view(), name = 'list-questions'),
    path('<int:pk>', QuestionDetailAPIView.as_view(), name = 'detail-question'),
    path('<int:q_pk>/<int:a_pk>', AnswerDetailAPIView.as_view(), name = 'detail-answer'),
    path('<int:pk>/save', SaveView.as_view(), name = 'save-question'),
    path('<int:pk>/support', SupportView.as_view(), name = 'support-question'),
    path('<int:q_pk>/<int:a_pk>/support', SupportView.as_view(), name = 'support-answer'),
]