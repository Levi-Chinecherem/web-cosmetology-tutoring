# progress/admin.py
from django.contrib import admin
from .models import QuizProgress, StudentProgress

class QuizProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'quiz', 'current_question',)
    list_filter = ('user', 'quiz',)
    search_fields = ('user__username', 'quiz__title',)

class StudentProgressAdmin(admin.ModelAdmin):
    list_display = ('student', 'quiz_attempt', 'score', 'timestamp',)
    list_filter = ('student', 'quiz_attempt',)
    search_fields = ('student__username', 'quiz_attempt__title',)

admin.site.register(QuizProgress, QuizProgressAdmin)
admin.site.register(StudentProgress, StudentProgressAdmin)
