from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Submission, Choice
from django.shortcuts import render
from .models import Course


def home(request):
    return HttpResponse("Hello, Django is working!")


def course_detail(request, course_id):
    course = Course.objects.get(id=course_id)
    return render(request, 'course_detail.html', {'course': course})

def submit_exam(request, course_id):
    if request.method == "POST":
        selected_choices = request.POST.getlist('choice')

        submission = Submission.objects.create(
            user=request.user,
            course_id=course_id
        )

        submission.choices.set(selected_choices)

        return redirect('exam_result', submission.id)
def calculate_score(submission):
    total = 0
    correct = 0

    for question in submission.course.question_set.all():
        total += 1

        correct_choices = question.choice_set.filter(is_correct=True)
        selected_choices = submission.choices.filter(question=question)

        if set(correct_choices) == set(selected_choices):
            correct += 1

    return (correct / total) * 100
def exam_result(request, submission_id):
    submission = Submission.objects.get(id=submission_id)
    score = calculate_score(submission)

    return render(request, 'exam_result.html', {
        'submission': submission,
        'score': score
    })