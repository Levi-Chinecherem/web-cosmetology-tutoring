from django.shortcuts import render, get_object_or_404
from .models import Quiz, Question, Answer
from django.contrib.auth.mixins import LoginRequiredMixin
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

# QUIZ VIEWS
@admin_required
@instructor_required
class QuizCreateView(LoginRequiredMixin, CreateView):
    model = Quiz
    fields = ['title', 'description']
    success_url = reverse_lazy('quiz-list')

    def form_valid(self, form):
        form.instance.creator = self.request.user  # Set the creator to the logged-in user
        return super().form_valid(form)

@admin_required
@instructor_required
class QuizUpdateView(LoginRequiredMixin, UpdateView):
    model = Quiz
    fields = ['title', 'description']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('quiz-list')

@admin_required
@instructor_required
class QuizDeleteView(LoginRequiredMixin, DeleteView):
    model = Quiz
    success_url = reverse_lazy('quiz-list')

# QUESTION VIEWS
@admin_required
@instructor_required
class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    fields = ['quiz', 'content']
    success_url = reverse_lazy('question-list')

@admin_required
@instructor_required
class QuestionUpdateView(LoginRequiredMixin, UpdateView):
    model = Question
    fields = ['quiz', 'content']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('question-list')

@admin_required
class QuestionDeleteView(LoginRequiredMixin, DeleteView):
    model = Question
    success_url = reverse_lazy('question-list')

# ANSWER VIEWS
@admin_required
@instructor_required
class AnswerCreateView(LoginRequiredMixin, CreateView):
    model = Answer
    fields = ['question', 'content', 'is_correct']
    success_url = reverse_lazy('answer-list')

@admin_required
@instructor_required
class AnswerUpdateView(LoginRequiredMixin, UpdateView):
    model = Answer
    fields = ['question', 'content', 'is_correct']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('answer-list')

@admin_required
@instructor_required
class AnswerDeleteView(LoginRequiredMixin, DeleteView):
    model = Answer
    success_url = reverse_lazy('answer-list')
