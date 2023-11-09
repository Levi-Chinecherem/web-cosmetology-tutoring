# instructors/admin.py
from django.contrib import admin
from .models import Instructor, QuizInstructor

class InstructorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'specialty', 'experience',)
    search_fields = ('name', 'email', 'specialty',)

class QuizInstructorAdmin(admin.ModelAdmin):
    list_display = ('instructor', 'quiz',)
    list_filter = ('instructor', 'quiz',)
    search_fields = ('instructor__name', 'quiz__title',)

admin.site.register(Instructor, InstructorAdmin)
admin.site.register(QuizInstructor, QuizInstructorAdmin)
