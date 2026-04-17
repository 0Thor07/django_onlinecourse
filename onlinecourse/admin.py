from django.contrib import admin
from .models import Course, Question, Choice, Submission, Instructor, Learner, Lesson

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course')

class CourseAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]

admin.site.register(Course, CourseAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Lesson, LessonAdmin)