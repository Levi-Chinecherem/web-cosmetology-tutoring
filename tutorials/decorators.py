# decorators.py
from functools import wraps
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse_lazy

def admin_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_superuser:
            return view_func(request, *args, **kwargs)
        return user_passes_test(lambda u: u.is_superuser, login_url=reverse_lazy('login'))(view_func)(request, *args, **kwargs)
    return _wrapped_view

def instructor_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.groups.filter(name='Instructors').exists():
            return view_func(request, *args, **kwargs)
        return user_passes_test(lambda u: u.groups.filter(name='Instructors').exists(), login_url=reverse_lazy('login'))(view_func)(request, *args, **kwargs)
    return _wrapped_view
