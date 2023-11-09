# videos/views.py
from django.shortcuts import render, get_object_or_404
from .models import Video, VideoCategory
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import user_passes_test

# Custom decorator for admin user required
def admin_required(view_func):
    def check_admin(user):
        return user.is_superuser

    return user_passes_test(check_admin, login_url=reverse_lazy('login'))(view_func)

# Custom decorator for instructor user required
def instructor_required(view_func):
    def check_instructor(user):
        return user.groups.filter(name='Instructors').exists()

    return user_passes_test(check_instructor, login_url=reverse_lazy('login'))(view_func)

# VIDEO VIEWS
class VideoListView(ListView):
    model = Video
    template_name = 'videos/video_list.html'
    context_object_name = 'videos'

class VideoDetailView(DetailView):
    model = Video
    template_name = 'videos/video_detail.html'
    context_object_name = 'video'

@admin_required
@instructor_required
class VideoCreateView(LoginRequiredMixin, CreateView):
    model = Video
    fields = ['title', 'description', 'video_url', 'category']
    success_url = reverse_lazy('video-list')

    def form_valid(self, form):
        form.instance.creator = self.request.user  # Set the creator to the logged-in user
        return super().form_valid(form)

@admin_required
@instructor_required
class VideoUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Video
    fields = ['title', 'description', 'video_url', 'category']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('video-list')
    permission_required = 'videos.can_change_video'  # Specify the correct permission name

@admin_required
@instructor_required
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

@admin_required
@instructor_required
class VideoCategoryCreateView(LoginRequiredMixin, CreateView):
    model = VideoCategory
    fields = ['name', 'description']
    success_url = reverse_lazy('video-category-list')

@admin_required
@instructor_required
class VideoCategoryUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = VideoCategory
    fields = ['name', 'description']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('video-category-list')
    permission_required = 'videos.can_change_videocategory'  # Specify the correct permission name

@admin_required
@instructor_required
class VideoCategoryDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = VideoCategory
    success_url = reverse_lazy('video-category-list')
    permission_required = 'videos.can_delete_videocategory'
