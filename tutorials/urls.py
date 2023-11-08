# tutorials/urls.py
from django.urls import path
from .views import (
    TutorialListView,
    TutorialDetailView,
    TutorialCreateView,
    TutorialUpdateView,
    TutorialDeleteView,
    StepListView,  # Add Step views
    StepDetailView,
    CategoryListView,  # Add Category views
    CategoryDetailView,
    StepCreateView,
    StepUpdateView,
    StepDeleteView,
    CategoryCreateView,
    CategoryUpdateView,
    CategoryDeleteView,
)
from . import views
app_name = 'tutorials'

urlpatterns = [
    # Tutorials URLs
    path('tutorials/', TutorialListView.as_view(), name='tutorial-list'),
    path('tutorials/<int:pk>/', TutorialDetailView.as_view(), name='tutorial-detail'),
    path('tutorials/create/', TutorialCreateView.as_view(), name='tutorial-create'),
    path('tutorials/<int:pk>/update/', TutorialUpdateView.as_view(), name='tutorial-update'),
    path('tutorials/<int:pk>/delete/', TutorialDeleteView.as_view(), name='tutorial-delete'),

    # Steps URLs
    path('steps/', StepListView.as_view(), name='step-list'),  # Add Step URLs
    path('steps/<int:pk>/', StepDetailView.as_view(), name='step-detail'),
    path('tutorials/<int:tutorial_id>/step/create/', views.StepCreateView.as_view(), name='step-create'),
    path('steps/<int:pk>/update/', StepUpdateView.as_view(), name='step-update'),
    path('steps/<int:pk>/delete/', StepDeleteView.as_view(), name='step-delete'),

    # Category URLs
    path('categories/', CategoryListView.as_view(), name='category-list'),  # Add Category URLs
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('categories/create/', CategoryCreateView.as_view(), name='category-create'),
    path('categories/<int:pk>/update/', CategoryUpdateView.as_view(), name='category-update'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category-delete'),
]
