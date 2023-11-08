from django.urls import path
from .views import StudentProgressListView
from . import views

urlpatterns = [
    path('progress/', StudentProgressListView.as_view(), name='student-progress-list'),
    path('start-quiz/<int:quiz_id>/', views.start_quiz, name='start-quiz'),
    path('continue-quiz/<int:quiz_id>/', views.continue_quiz, name='continue-quiz'),
    path('answer-question/<int:quiz_id>/<int:question_id>/', views.answer_question, name='answer-question'),
]