from django.contrib import admin
from django.urls import path

from.views import course_list, course_detail, lesson_detail

urlpatterns = [
    path('', course_list, name='course_list'),
    path('course/<int:course_id>/', course_detail, name='course_detail'),
    path('lesson/<int:lesson_id>/', lesson_detail, name='lesson_detail'),
]