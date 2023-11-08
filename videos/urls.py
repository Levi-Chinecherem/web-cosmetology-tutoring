# videos/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Video URLs
    path('videos/', views.VideoListView.as_view(), name='video-list'),
    path('videos/<int:pk>/', views.VideoDetailView.as_view(), name='video-detail'),
    path('videos/create/', views.VideoCreateView.as_view(), name='video-create'),
    path('videos/<int:pk>/update/', views.VideoUpdateView.as_view(), name='video-update'),
    path('videos/<int:pk>/delete/', views.VideoDeleteView.as_view(), name='video-delete'),
    
    # Video Category URLs
    path('video-categories/', views.VideoCategoryListView.as_view(), name='video-category-list'),
    path('video-categories/<int:pk>/', views.VideoCategoryDetailView.as_view(), name='video-category-detail'),
    path('video-categories/create/', views.VideoCategoryCreateView.as_view(), name='video-category-create'),
    path('video-categories/<int:pk>/update/', views.VideoCategoryUpdateView.as_view(), name='video-category-update'),
    path('video-categories/<int:pk>/delete/', views.VideoCategoryDeleteView.as_view(), name='video-category-delete'),
]
