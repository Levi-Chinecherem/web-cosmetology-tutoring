from django.shortcuts import render, get_object_or_404
from .models import Quiz, Question, Answer
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import user_passes_test
from tutorials.decorators import admin_required, instructor_required
from django.utils.decorators import method_decorator

# QUIZ VIEWS
class QuizListView(ListView):
    model = Quiz
    template_name = 'quizzes/quiz_list.html'
    context_object_name = 'quizzes'

class QuizDetailView(DetailView):
    model = Quiz
    template_name = 'quizzes/quiz_detail.html'
    context_object_name = 'quiz'

class QuizCreateView(LoginRequiredMixin, CreateView):
    model = Quiz
    fields = ['title', 'description']
    template_name = 'quizzes/quiz_form.html'
    success_url = reverse_lazy('quiz-list')

    @method_decorator(admin_required)
    @method_decorator(instructor_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.creator = self.request.user  # Set the creator to the logged-in user
        return super().form_valid(form)

class QuizUpdateView(LoginRequiredMixin, UpdateView):
    model = Quiz
    fields = ['title', 'description']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('quiz-list')

    @method_decorator(admin_required)
    @method_decorator(instructor_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class QuizDeleteView(LoginRequiredMixin, DeleteView):
    model = Quiz
    template_name = 'quizzes/quiz_confirm_delete.html'
    success_url = reverse_lazy('quiz-list')

    @method_decorator(admin_required)
    @method_decorator(instructor_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

# QUESTION VIEWS
class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    fields = ['quiz', 'content']
    success_url = reverse_lazy('question-list')

    @method_decorator(admin_required)
    @method_decorator(instructor_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class QuestionUpdateView(LoginRequiredMixin, UpdateView):
    model = Question
    fields = ['quiz', 'content']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('question-list')

    @method_decorator(admin_required)
    @method_decorator(instructor_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class QuestionDeleteView(LoginRequiredMixin, DeleteView):
    model = Question
    success_url = reverse_lazy('question-list')

    @method_decorator(admin_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

# ANSWER VIEWS
class AnswerCreateView(LoginRequiredMixin, CreateView):
    model = Answer
    fields = ['question', 'content', 'is_correct']
    success_url = reverse_lazy('answer-list')

    @method_decorator(admin_required)
    @method_decorator(instructor_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class AnswerUpdateView(LoginRequiredMixin, UpdateView):
    model = Answer
    fields = ['question', 'content', 'is_correct']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('answer-list')

    @method_decorator(admin_required)
    @method_decorator(instructor_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class AnswerDeleteView(LoginRequiredMixin, DeleteView):
    model = Answer
    success_url = reverse_lazy('answer-list')

    @method_decorator(admin_required)
    @method_decorator(instructor_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
