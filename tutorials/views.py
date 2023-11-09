# tutorials/views.py
from django.shortcuts import render, get_object_or_404
from .models import Tutorial, Step, Category
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import StepForm
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

# TUTORIAL VIEWS
class TutorialListView(ListView):
    model = Tutorial
    template_name = 'tutorials/tutorial_list.html'
    context_object_name = 'tutorials'

class TutorialDetailView(DetailView):
    model = Tutorial
    template_name = 'tutorials/tutorial_detail.html'
    context_object_name = 'tutorial'

@admin_required
@instructor_required
class TutorialCreateView(LoginRequiredMixin, CreateView):
    model = Tutorial
    fields = ['title', 'image', 'category', 'description']
    success_url = reverse_lazy('tutorial-list')

    def form_valid(self, form):
        form.instance.creator = self.request.user  # Set the creator to the logged-in user
        return super().form_valid(form)

@admin_required
@instructor_required
class TutorialUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Tutorial
    fields = ['title', 'image', 'category', 'description']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('tutorial-list')
    permission_required = 'tutorials.can_change_tutorial'  # Adjust the correct permission name

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['creator'] = self.request.user  # Pass the creator to the form
        return kwargs

@admin_required
@instructor_required
class TutorialDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Tutorial
    success_url = reverse_lazy('tutorial-list')
    permission_required = 'tutorials.can_delete_tutorial'  

# STEPS VIEWS
class StepListView(ListView):
    model = Step
    template_name = 'tutorials/step_list.html'
    context_object_name = 'steps'

class StepDetailView(DetailView):
    model = Step
    template_name = 'tutorials/step_detail.html'
    context_object_name = 'step'

@admin_required
@instructor_required
class StepCreateView(LoginRequiredMixin, CreateView):
    model = Step
    form_class = StepForm  # Use the updated StepForm
    template_name = 'tutorials/step_form.html'
    permission_required = 'tutorials.can_create_step'

    def form_valid(self, form):
        tutorial = get_object_or_404(Tutorial, pk=self.kwargs['tutorial_id'])
        form.instance.tutorial = tutorial  # Set the tutorial for the step
        form.instance.creator = self.request.user  # Set the creator to the logged-in user
        form.instance.order = form.cleaned_data['order']  # Set the order from the form
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('tutorial-detail', args=[self.kwargs['tutorial_id']])

@admin_required
@instructor_required
class StepUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Step
    fields = ['tutorial', 'order', 'title', 'content']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('step-list')
    permission_required = 'tutorials.can_change_step'  # Specify the correct permission name

@admin_required
@instructor_required
class StepDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Step
    success_url = reverse_lazy('step-list')
    permission_required = 'tutorials.can_delete_step' 

# Category VIEWS
class CategoryListView(ListView):
    model = Category
    template_name = 'tutorials/category_list.html'
    context_object_name = 'categories'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'tutorials/category_detail.html'
    context_object_name = 'category'

@admin_required
@instructor_required
class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    fields = ['name', 'description']
    success_url = reverse_lazy('category-list')

@admin_required
@instructor_required
class CategoryUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Category
    fields = ['name', 'description']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('category-list')
    permission_required = 'tutorials.can_change_category'  # Specify the correct permission name

@admin_required
@instructor_required
class CategoryDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Category
    success_url = reverse_lazy('category-list')
    permission_required = 'tutorials.can_delete_category' 
