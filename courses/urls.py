from django.shortcuts import render
from django.template import loader
from django.urls import path

from .views import CourseDetailView, CourseCreateView, course, CourseDeleteView, CourseUpdateView, CourseListView

urlpatterns = [
    path('', course, name='course'),
 # Create a new course
    path('create/',CourseCreateView.as_view(), name='course-create'),

    # Detail view of a specific course
    path('detail/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('delete/<int:pk>', CourseDeleteView.as_view(),name='course-delete'),
    path('update/<int:pk>', CourseUpdateView.as_view(), name='course-update'),
    path('list/', CourseListView.as_view(), name='course-list')

]
