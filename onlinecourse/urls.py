from django.urls import path
from . import views

urlpatterns = [
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    path('result/<int:submission_id>/', views.exam_result, name='exam_result'),
    path('submit/<int:course_id>/', views.submit_exam, name='submit_exam'),
    path('result/<int:submission_id>/', views.exam_result, name='exam_result'),
]
