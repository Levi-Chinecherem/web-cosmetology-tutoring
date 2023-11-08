from django.db import models
from django.contrib.auth.models import User

class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    specialty = models.CharField(max_length=100)
    experience = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

class QuizInstructor(models.Model):
    quiz = models.ForeignKey('quizzes.Quiz', on_delete=models.CASCADE)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.instructor} - {self.quiz}"
