# quizzes/admin.py
from django.contrib import admin
from .models import Quiz, Question, Answer

class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'creator', 'created_at',)
    list_filter = ('creator',)
    search_fields = ('title', 'description', 'creator__user__username',)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('quiz', 'content', 'created_at',)
    list_filter = ('quiz',)
    search_fields = ('content', 'quiz__title',)

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'content', 'is_correct',)
    list_filter = ('question__quiz',)
    search_fields = ('content', 'question__content',)

admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
