from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Instructor, QuizInstructor
from django.urls import reverse_lazy
from tutorials.decorators import admin_required, instructor_required
from django.utils.decorators import method_decorator

class InstructorListView(ListView):
    model = Instructor
    template_name = 'instructors/instructor_list.html'
    context_object_name = 'instructors'

class InstructorDetailView(DetailView):
    model = Instructor
    template_name = 'instructors/instructor_detail.html'
    context_object_name = 'instructor'

class InstructorCreateView(CreateView):
    model = Instructor
    fields = ['user', 'name', 'email', 'specialty', 'experience']
    template_name = 'instructors/instructor_form.html'

    @method_decorator(admin_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class InstructorUpdateView(UpdateView):
    model = Instructor
    fields = ['user', 'name', 'email', 'specialty', 'experience']
    template_name = 'instructors/instructor_form.html'

    @method_decorator(admin_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class InstructorDeleteView(DeleteView):
    model = Instructor
    template_name = 'instructors/instructor_confirm_delete.html'
    success_url = reverse_lazy('instructor-list')

    @method_decorator(admin_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

# QuizInstructor Views
class QuizInstructorListView(ListView):
    model = QuizInstructor
    template_name = 'instructors/quiz_instructor_list.html'
    context_object_name = 'quiz_instructors'

class QuizInstructorDetailView(DetailView):
    model = QuizInstructor
    template_name = 'instructors/quiz_instructor_detail.html'
    context_object_name = 'quiz_instructor'

class QuizInstructorCreateView(CreateView):
    model = QuizInstructor
    fields = ['quiz', 'instructor']
    success_url = reverse_lazy('quiz-instructor-list')

    @method_decorator(admin_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class QuizInstructorUpdateView(UpdateView):
    model = QuizInstructor
    fields = ['quiz', 'instructor']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('quiz-instructor-list')

    @method_decorator(admin_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class QuizInstructorDeleteView(DeleteView):
    model = QuizInstructor
    success_url = reverse_lazy('quiz-instructor-list')

    @method_decorator(admin_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
