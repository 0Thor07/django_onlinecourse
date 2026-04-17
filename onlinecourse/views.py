from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Submission, Choice

# Show course details (with questions & choices)
def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'course_details_bootstrap.html', {'course': course})


# Handle exam submission
def submit_exam(request, course_id):
    course = get_object_or_404(Course, pk=course_id)

    if request.method == 'POST':
        selected_choices = request.POST.getlist('choice')

        # Create submission
        submission = Submission.objects.create(course=course, user=None)

        # Add selected choices
        for choice_id in selected_choices:
            choice = Choice.objects.get(id=int(choice_id))
            submission.choices.add(choice)

        submission.save()

        return redirect('show_exam_result', submission_id=submission.id)

    return redirect('course_detail', course_id=course.id)


# Show exam result
def show_exam_result(request, submission_id):
    submission = get_object_or_404(Submission, pk=submission_id)
    course = submission.course

    selected_choices = submission.choices.all()

    total = 0
    correct = 0

    # Calculate score
    for question in course.question_set.all():
        for choice in question.choice_set.all():
            if choice.is_correct:
                total += 1
                if choice in selected_choices:
                    correct += 1

    score = (correct / total) * 100 if total > 0 else 0

    return render(request, 'exam_result.html', {
        'submission': submission,
        'course': course,
        'score': score,
    })