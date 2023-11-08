
# progress/views.py
from django.shortcuts import render, redirect
from .models import QuizProgress
from quizzes.models import Quiz, Question, Answer
from django.views.generic import ListView
from .models import StudentProgress
from django.urls import reverse

# Progress Views
class StudentProgressListView(ListView):
    model = StudentProgress
    template_name = 'progress/student_progress_list.html'
    context_object_name = 'student_progress'

def start_quiz(request, quiz_id):
    # Retrieve the quiz and initialize progress
    quiz = Quiz.objects.get(pk=quiz_id)
    progress, created = QuizProgress.objects.get_or_create(user=request.user, quiz=quiz)
    if created:
        # Set the initial question as the current question
        progress.current_question = quiz.questions.first()
        progress.save()
    return redirect('continue-quiz', quiz_id=quiz_id)

def continue_quiz(request, quiz_id):
    # Retrieve the quiz and progress
    quiz = Quiz.objects.get(pk=quiz_id)
    progress, _ = QuizProgress.objects.get_or_create(user=request.user, quiz=quiz)
    current_question = progress.current_question
    if current_question:
        # Display the current question to the user
        return render(request, 'progress/question.html', {'question': current_question})
    else:
        # Quiz completed
        return render(request, 'progress/quiz_completed.html')

def answer_question(request, quiz_id, question_id):
    # Handle user's answer and update progress
    quiz = Quiz.objects.get(pk=quiz_id)
    question = Question.objects.get(pk=question_id)
    selected_answer = request.POST.get('answer')  # Retrieve selected answer
    # Add logic to check if the answer is correct
    is_correct = True  # Replace with actual logic
    if is_correct:
        progress, _ = QuizProgress.objects.get_or_create(user=request.user, quiz=quiz)
        progress.answered_questions.add(question)  # Mark the question as answered
        progress.current_question = get_next_unanswered_question(quiz, progress)
        progress.save()
    return redirect('continue-quiz', quiz_id=quiz_id)

def get_next_unanswered_question(quiz, progress):
    # Get all questions in the quiz
    all_questions = quiz.questions.all()

    # Filter out the questions that the user has already answered
    answered_questions = progress.answered_questions.all()

    # Find the first unanswered question
    for question in all_questions:
        if question not in answered_questions:
            return reverse('answer', args=[quiz.id, question.id])  # Redirect to answer page

    # If all questions have been answered, return the result page
    return reverse('quiz-result', args=[quiz.id])
