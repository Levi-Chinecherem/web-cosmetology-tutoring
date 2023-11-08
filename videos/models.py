# videos/models.py
from django.db import models
from ckeditor.fields import RichTextUploadingField
from django.contrib.auth.models import User

class VideoCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str(self):
        return self.name

class Video(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextUploadingField()  # Use CKEditor for rich text content
    video_url = models.URLField()
    category = models.ForeignKey(VideoCategory, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)  # Add a creator field

    def __str__(self):
        return self.title
