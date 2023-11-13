from django.urls import path
from .views import QuizListView, QuizDetailView, QuizCreateView, QuizUpdateView, QuizDeleteView
from .views import QuestionCreateView, QuestionUpdateView, QuestionDeleteView
from .views import AnswerCreateView, QuestionDetailView, AnswerUpdateView, ScoreQuestionView, AnswerDeleteView

urlpatterns = [
    path('quizzes/', QuizListView.as_view(), name='quiz-list'),
    path('quiz/<int:pk>/', QuizDetailView.as_view(), name='quiz-detail'),
    path('quiz/create/', QuizCreateView.as_view(), name='quiz-create'),
    path('quiz/<int:pk>/update/', QuizUpdateView.as_view(), name='quiz-update'),
    path('quiz/<int:pk>/delete/', QuizDeleteView.as_view(), name='quiz-delete'),

    path('questions/create/', QuestionCreateView.as_view(), name='question-create'),
    path('question/<int:pk>/', QuestionDetailView.as_view(), name='question_detail'),
    path('question/<int:pk>/score/', ScoreQuestionView.as_view(), name='score_question'),
    path('question/<int:pk>/update/', QuestionUpdateView.as_view(), name='question-update'),
    path('question/<int:pk>/delete/', QuestionDeleteView.as_view(), name='question-delete'),

    path('answers/create/', AnswerCreateView.as_view(), name='answer-create'),
    path('answer/<int:pk>/update/', AnswerUpdateView.as_view(), name='answer-update'),
    path('answer/<int:pk>/delete/', AnswerDeleteView.as_view(), name='answer-delete'),
]
