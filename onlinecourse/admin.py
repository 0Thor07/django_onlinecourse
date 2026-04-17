from django.contrib import admin
from .models import Course, Question, Choice, Submission

# Inline for Choice
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

# Inline for Question
class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1

# Question Admin
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

# Course Admin
class CourseAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]

admin.site.register(Course, CourseAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
from .models import Instructor, Learner, Lesson

admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Lesson)