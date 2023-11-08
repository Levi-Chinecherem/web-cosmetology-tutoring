# tutorials/admin.py
from django.contrib import admin
from .models import Category, Tutorial, Step

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')

class TutorialAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'image', 'description')
    list_filter = ('category',)
    search_fields = ('title', 'category__name')
    list_per_page = 20

class StepAdmin(admin.ModelAdmin):
    list_display = ('title', 'tutorial', 'order', 'content')
    list_filter = ('tutorial',)
    search_fields = ('title', 'tutorial__title')
    list_per_page = 20

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tutorial, TutorialAdmin)
admin.site.register(Step, StepAdmin)

# Customize the Django admin branding and titles
admin.site.site_header = "Cosmetology Tutoring Administration"
admin.site.site_title = "Cosmetology Tutoring Admin"
admin.site.index_title = "Welcome to Cosmetology Tutoring"
admin.site.site_url = "/cosmetology-tutoring/"
