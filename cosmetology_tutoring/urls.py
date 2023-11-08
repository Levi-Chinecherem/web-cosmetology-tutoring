from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),  # Include the 'home' app's URLs for the homepage
    path('account/', include('account.urls')),  # Include the 'account' app's URLs for authentication
    path('tutorials/', include('tutorials.urls')),  # Include the 'tutorials' app's URLs
    path('videos/', include('videos.urls')),  # Include the 'videos' app's URLs
    path('quizzes/', include('quizzes.urls')),  # Include the 'quizzes' app's URLs
    path('instructors/', include('instructors.urls')),  # Include the 'instructors' app's URLs
    path('progress/', include('progress.urls')),  # Include the 'progress' app's URLs
]
