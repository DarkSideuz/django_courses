from django.contrib import admin
from django.urls import path

from.views import course_list, course_detail, lesson_detail, add_course, add_lesson, update_course, update_lesson

urlpatterns = [
    path('', course_list, name='course_list'),
    path('course/<int:course_id>/', course_detail, name='course_detail'),
    path('lesson/<int:lesson_id>/', lesson_detail, name='lesson_detail'),
    path('addcourse/', add_course, name='add_course'),
    path('addlesson/', add_lesson, name='add_lesson'),
    path('course/<int:course_id>/edit/', update_course, name='update_course'),
    path('lesson/<int:lesson_id>/edit/', update_lesson, name='update_lesson'),
]