from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model  # Correct import

User = get_user_model()  # Get the user model dynamically

# Custom registration view
class SignupView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')  # Redirect to the login page after successful registration

# Custom login view extending the built-in view
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'  # Customize the login template as needed
    success_url = '/dashboard/'  # Redirect to the user's dashboard or homepage upon successful login

# Custom logout view extending the built-in view
class CustomLogoutView(LogoutView):
    next_page = '/login/'  # Redirect to the login page after logout

# Custom password change view extending the built-in view
class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'registration/password_change.html'  # Customize the password change template as needed
    success_url = reverse_lazy('password_change_done')

# Custom password change done view extending the built-in view
class CustomPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'registration/password_change_done.html'  # Customize the password change done template as needed

# Custom password reset view extending the built-in view
class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset.html'  # Customize the password reset template as needed
    email_template_name = 'registration/password_reset_email.html'  # Customize the email template

# Custom password reset done view extending the built-in view
class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'registration/password_reset_done.html'  # Customize the password reset done template as needed

# Custom password reset confirm view extending the built-in view
class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm.html'  # Customize the password reset confirm template as needed

# Custom password reset complete view extending the built-in view
class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'registration/password_reset_complete.html'  # Customize the password reset complete template as needed
