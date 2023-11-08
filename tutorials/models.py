from django.db import models
from ckeditor.fields import RichTextUploadingField
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)  # Add a creator field

    class Meta:
        permissions = [
            ("can_change_category", "Can change category"),
            ("can_delete_category", "Can delete category"),
        ]

    def __str__(self):
        return self.name

class Tutorial(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='tutorial_images/')  # Use ImageField for images
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = RichTextUploadingField()  # Use CKEditor for rich text content

    def __str__(self):
        return self.title

class Step(models.Model):
    tutorial = models.ForeignKey(Tutorial, on_delete=models.CASCADE)
    order = models.PositiveIntegerField()
    title = models.CharField(max_length=200)
    content = RichTextUploadingField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)  # Add a creator field

    class Meta:
        permissions = [
            ("can_change_step", "Can change step"),
            ("can_delete_step", "Can delete step"),
        ]

    def __str__(self):
        return self.title
