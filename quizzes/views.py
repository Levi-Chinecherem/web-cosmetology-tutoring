from django.shortcuts import render, get_object_or_404
from .models import Quiz, Question, Answer
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import user_passes_test
from tutorials.decorators import admin_required, instructor_required
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.views import View
from progress.models import QuizProgress, StudentProgress

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

class QuestionDetailView(DetailView):
    model = Question
    template_name = 'quizzes/question_detail.html'
    context_object_name = 'question'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        answers = Answer.objects.filter(question=context['question'])
        context['answers'] = answers
        return context

    def post(self, request, *args, **kwargs):
        question = self.get_object()
        selected_answer_id = request.POST.get('selected_answer')
        selected_answer = get_object_or_404(Answer, pk=selected_answer_id)
        
        is_correct = selected_answer.is_correct

        # Update progress
        quiz_progress, created = QuizProgress.objects.get_or_create(
            user=self.request.user,
            quiz=question.quiz  # Include the quiz in the filter
        )
        quiz_progress.answered_questions.add(question)
        quiz_progress.current_question = None
        quiz_progress.save()

        # Update or create student progress
        student_progress, created = StudentProgress.objects.get_or_create(
            student=self.request.user,
            quiz_attempt=question.quiz
        )
        if is_correct:
            student_progress.score += 1
        student_progress.save()

        # Prepare context for rendering the template
        answers = Answer.objects.filter(question=question)
        context = {'question': question, 'answers': answers, 'score': student_progress.score}

        # Prepare JSON response
        response_data = {
            'is_correct': is_correct,
            'score': student_progress.score,
            'questions_left': Question.objects.filter(quiz=question.quiz).exclude(id__in=quiz_progress.answered_questions.all()).count()
        }

        # If the request is AJAX, return JSON response
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse(response_data)

        # If not AJAX, render the template with the updated context
        return render(request, self.template_name, context)

class ScoreQuestionView(View):
    def get(self, request, *args, **kwargs):
        # Handle GET requests here
        return JsonResponse({'message': 'GET requests are not allowed for this endpoint.'}, status=405)

    def post(self, request, *args, **kwargs):
        if not request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'message': 'Invalid request.'}, status=400)

        question_id = kwargs.get('pk')
        question = get_object_or_404(Question, pk=question_id)
        
        # For demonstration purposes, assuming the selected answer ID is sent in the POST data.
        selected_answer_id = request.POST.get('selected_answer')
        selected_answer = get_object_or_404(Answer, pk=selected_answer_id)

        # Perform scoring logic here...
        is_correct = selected_answer.is_correct

        # Return JSON response
        return JsonResponse({'is_correct': is_correct})


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
