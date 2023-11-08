from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse

# Custom decorator for admin user required
def admin_required(view_func):
    def check_admin(user):
        return user.is_superuser

    return user_passes_test(check_admin, login_url=reverse('login'))(view_func)

# Custom decorator for instructor user required
def instructor_required(view_func):
    def check_instructor(user):
        return user.groups.filter(name='Instructors').exists()

    return user_passes_test(check_instructor, login_url=reverse('login'))(view_func)
