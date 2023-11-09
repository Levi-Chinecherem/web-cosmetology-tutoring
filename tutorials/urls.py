# cosmetology_tutoring/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Tutorials URLs
    path('', views.TutorialListView.as_view(), name='tutorial-list'),
    path('<int:pk>/', views.TutorialDetailView.as_view(), name='tutorial-detail'),
    path('create/', views.TutorialCreateView.as_view(), name='tutorial-create'),
    path('<int:pk>/update/', views.TutorialUpdateView.as_view(), name='tutorial-update'),
    path('<int:pk>/delete/', views.TutorialDeleteView.as_view(), name='tutorial-delete'),

    # Steps URLs
    path('steps/', views.StepListView.as_view(), name='step-list'),
    path('steps/<int:pk>/', views.StepDetailView.as_view(), name='step-detail'),
    path('<int:tutorial_id>/step/create/', views.StepCreateView.as_view(), name='step-create'),
    path('steps/<int:pk>/update/', views.StepUpdateView.as_view(), name='step-update'),
    path('steps/<int:pk>/delete/', views.StepDeleteView.as_view(), name='step-delete'),

    # Category URLs
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', views.CategoryDetailView.as_view(), name='category-detail'),
    path('categories/create/', views.CategoryCreateView.as_view(), name='category-create'),
    path('categories/<int:pk>/update/', views.CategoryUpdateView.as_view(), name='category-update'),
    path('categories/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category-delete'),
]
