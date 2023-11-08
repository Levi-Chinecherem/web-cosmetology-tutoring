# progress/urls.py
from django.urls import path
from .views import (
    InstructorListView, InstructorDetailView, InstructorCreateView,
    InstructorUpdateView, InstructorDeleteView,
    QuizInstructorListView, QuizInstructorDetailView, QuizInstructorCreateView,
    QuizInstructorUpdateView, QuizInstructorDeleteView,
)

urlpatterns = [
    # Instructor URLs
    path('instructors/', InstructorListView.as_view(), name='instructor-list'),
    path('instructors/<int:pk>/', InstructorDetailView.as_view(), name='instructor-detail'),
    path('instructors/create/', InstructorCreateView.as_view(), name='instructor-create'),
    path('instructors/<int:pk>/update/', InstructorUpdateView.as_view(), name='instructor-update'),
    path('instructors/<int:pk>/delete/', InstructorDeleteView.as_view(), name='instructor-delete'),

    # QuizInstructor URLs
    path('quiz-instructors/', QuizInstructorListView.as_view(), name='quiz-instructor-list'),
    path('quiz-instructors/<int:pk>/', QuizInstructorDetailView.as_view(), name='quiz-instructor-detail'),
    path('quiz-instructors/create/', QuizInstructorCreateView.as_view(), name='quiz-instructor-create'),
    path('quiz-instructors/<int:pk>/update/', QuizInstructorUpdateView.as_view(), name='quiz-instructor-update'),
    path('quiz-instructors/<int:pk>/delete/', QuizInstructorDeleteView.as_view(), name='quiz-instructor-delete'),
]
