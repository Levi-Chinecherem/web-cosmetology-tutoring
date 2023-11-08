from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Instructor, QuizInstructor
from django.urls import reverse_lazy
from .decorators import admin_required, instructor_required  # Import the decorators

class InstructorListView(ListView):
    model = Instructor
    template_name = 'instructors/instructor_list.html'
    context_object_name = 'instructors'

class InstructorDetailView(DetailView):
    model = Instructor
    template_name = 'instructors/instructor_detail.html'
    context_object_name = 'instructor'

@admin_required
class InstructorCreateView(CreateView):
    model = Instructor
    fields = ['user', 'name', 'email', 'specialty', 'experience']
    template_name = 'instructors/instructor_form.html'

@admin_required
class InstructorUpdateView(UpdateView):
    model = Instructor
    fields = ['user', 'name', 'email', 'specialty', 'experience']
    template_name = 'instructors/instructor_form.html'

@admin_required
class InstructorDeleteView(DeleteView):
    model = Instructor
    template_name = 'instructors/instructor_confirm_delete.html'
    success_url = reverse_lazy('instructor-list')

# QuizInstructor Views
class QuizInstructorListView(ListView):
    model = QuizInstructor
    template_name = 'instructors/quiz_instructor_list.html'
    context_object_name = 'quiz_instructors'

class QuizInstructorDetailView(DetailView):
    model = QuizInstructor
    template_name = 'instructors/quiz_instructor_detail.html'
    context_object_name = 'quiz_instructor'

@admin_required
class QuizInstructorCreateView(CreateView):
    model = QuizInstructor
    fields = ['quiz', 'instructor']
    success_url = reverse_lazy('quiz-instructor-list')

@admin_required
class QuizInstructorUpdateView(UpdateView):
    model = QuizInstructor
    fields = ['quiz', 'instructor']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('quiz-instructor-list')

@admin_required
class QuizInstructorDeleteView(DeleteView):
    model = QuizInstructor
    success_url = reverse_lazy('quiz-instructor-list')
