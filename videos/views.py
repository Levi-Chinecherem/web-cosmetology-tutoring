# videos/views.py
from django.shortcuts import render, get_object_or_404
from .models import Video, VideoCategory
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

# VIDEO VIEWS
class VideoListView(ListView):
    model = Video
    template_name = 'videos/video_list.html'
    context_object_name = 'videos'

class VideoDetailView(DetailView):
    model = Video
    template_name = 'videos/video_detail.html'
    context_object_name = 'video'

class VideoCreateView(LoginRequiredMixin, CreateView):
    model = Video
    fields = ['title', 'description', 'video_url', 'category']
    success_url = reverse_lazy('video-list')

    def form_valid(self, form):
        form.instance.creator = self.request.user  # Set the creator to the logged-in user
        return super().form_valid(form)

class VideoUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Video
    fields = ['title', 'description', 'video_url', 'category']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('video-list')
    permission_required = 'videos.can_change_video'  # Specify the correct permission name

class VideoDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Video
    success_url = reverse_lazy('video-list')
    permission_required = 'videos.can_delete_video' 

# VIDEO CATEGORY VIEWS
class VideoCategoryListView(ListView):
    model = VideoCategory
    template_name = 'videos/video_category_list.html'
    context_object_name = 'video_categories'

class VideoCategoryDetailView(DetailView):
    model = VideoCategory
    template_name = 'videos/video_category_detail.html'
    context_object_name = 'video_category'

class VideoCategoryCreateView(LoginRequiredMixin, CreateView):
    model = VideoCategory
    fields = ['name', 'description']
    success_url = reverse_lazy('video-category-list')

class VideoCategoryUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = VideoCategory
    fields = ['name', 'description']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('video-category-list')
    permission_required = 'videos.can_change_videocategory'  # Specify the correct permission name

class VideoCategoryDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = VideoCategory
    success_url = reverse_lazy('video-category-list')
    permission_required = 'videos.can_delete_videocategory'
