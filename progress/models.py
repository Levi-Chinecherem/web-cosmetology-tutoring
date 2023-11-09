# progress/models.py
from django.db import models
from django.contrib.auth.models import User
from quizzes.models import Quiz, Question, Answer

class QuizProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    current_question = models.ForeignKey(
        'quizzes.Question',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='current_question_progress'
    )

    answered_questions = models.ManyToManyField(
        'quizzes.Question',
        related_name='answered_questions_progress'
    )

    def __str__(self):
        return f"{self.user.username}'s current question {self.current_question}"

class StudentProgress(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the student/user
    quiz_attempt = models.ForeignKey(Quiz, on_delete=models.CASCADE)  # Link to the quiz attempt
    score = models.PositiveIntegerField()  # Track the score or progress
    timestamp = models.DateTimeField(auto_now_add=True)  # Track when the progress was made

    def __str__(self):
        return f"{self.student.username}'s progress for {self.quiz_attempt.title}"

