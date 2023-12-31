# tutorials/views.py
from django.shortcuts import render, get_object_or_404
from .models import Tutorial, Step, Category
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import StepForm
from django.contrib.auth.decorators import user_passes_test
from .decorators import admin_required, instructor_required
from django.utils.decorators import method_decorator

# TUTORIAL VIEWS
class TutorialListView(ListView):
    model = Tutorial
    template_name = 'tutorials/tutorial_list.html'
    context_object_name = 'tutorials'

class TutorialDetailView(DetailView):
    model = Tutorial
    template_name = 'tutorials/tutorial_detail.html'
    context_object_name = 'tutorial'

class TutorialCreateView(LoginRequiredMixin, CreateView):
    model = Tutorial
    fields = ['title', 'image', 'category', 'description']
    success_url = reverse_lazy('tutorial-list')

    @method_decorator(admin_required)
    @method_decorator(instructor_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.creator = self.request.user  # Set the creator to the logged-in user
        return super().form_valid(form)

class TutorialUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Tutorial
    fields = ['title', 'image', 'category', 'description']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('tutorial-list')
    permission_required = 'tutorials.can_change_tutorial'  # Adjust the correct permission name

    @method_decorator(admin_required)
    @method_decorator(instructor_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['creator'] = self.request.user  # Pass the creator to the form
        return kwargs

class TutorialDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Tutorial
    success_url = reverse_lazy('tutorial-list')
    permission_required = 'tutorials.can_delete_tutorial'  

    @method_decorator(admin_required)
    @method_decorator(instructor_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

# STEPS VIEWS
class StepListView(ListView):
    model = Step
    template_name = 'tutorials/step_list.html'
    context_object_name = 'steps'

class StepDetailView(DetailView):
    model = Step
    template_name = 'tutorials/step_detail.html'
    context_object_name = 'step'

class StepCreateView(LoginRequiredMixin, CreateView):
    model = Step
    form_class = StepForm  # Use the updated StepForm
    template_name = 'tutorials/step_form.html'
    permission_required = 'tutorials.can_create_step'

    @method_decorator(admin_required)
    @method_decorator(instructor_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        tutorial = get_object_or_404(Tutorial, pk=self.kwargs['tutorial_id'])
        form.instance.tutorial = tutorial  # Set the tutorial for the step
        form.instance.creator = self.request.user  # Set the creator to the logged-in user
        form.instance.order = form.cleaned_data['order']  # Set the order from the form
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('tutorial-detail', args=[self.kwargs['tutorial_id']])

class StepUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Step
    fields = ['tutorial', 'order', 'title', 'content']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('step-list')
    permission_required = 'tutorials.can_change_step'  # Specify the correct permission name

    @method_decorator(admin_required)
    @method_decorator(instructor_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class StepDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Step
    success_url = reverse_lazy('step-list')
    permission_required = 'tutorials.can_delete_step' 

    @method_decorator(admin_required)
    @method_decorator(instructor_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

# Category VIEWS
class CategoryListView(ListView):
    model = Category
    template_name = 'tutorials/category_list.html'
    context_object_name = 'categories'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'tutorials/category_detail.html'
    context_object_name = 'category'

class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    fields = ['name', 'description']
    success_url = reverse_lazy('category-list')

    @method_decorator(admin_required)
    @method_decorator(instructor_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class CategoryUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Category
    fields = ['name', 'description']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('category-list')
    permission_required = 'tutorials.can_change_category'  # Specify the correct permission name

    @method_decorator(admin_required)
    @method_decorator(instructor_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class CategoryDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Category
    success_url = reverse_lazy('category-list')
    permission_required = 'tutorials.can_delete_category' 

    @method_decorator(admin_required)
    @method_decorator(instructor_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
