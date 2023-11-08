# videos/admin.py
from django.contrib import admin
from .models import Video, VideoCategory

@admin.register(VideoCategory)
class VideoCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
    list_filter = ('name',)
    prepopulated_fields = {'name': ('name',)}  # Generates a slug from the name

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'category', 'creator')
    search_fields = ('title', 'category__name', 'creator__username')
    list_filter = ('category__name', 'creator__username')
    list_select_related = ('category', 'creator')
