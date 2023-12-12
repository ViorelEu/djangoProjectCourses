# urls.py

from django.urls import path
from .views import (
    CategoryCreateView,
    CategoryListView,
    CourseCreateView,
    CourseDeleteView,
    CourseDetailView,
    CourseListView,
    CourseUpdateView,
    EnrollmentCreateView,
    EnrollmentListView,
    InstructorCreateView,
    InstructorListView,
    LectureCreateView,
    LectureListView,
    RatingCreateView,
    RatingListView,
    SectionCreateView,
    SectionListView,
    TagCreateView,
    TagListView,
)

urlpatterns = [
    # Category URLs
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/create/', CategoryCreateView.as_view(), name='category-create'),

    # Course URLs
    path('courses/', CourseListView.as_view(), name='course-list'),
    path('courses/create/', CourseCreateView.as_view(), name='course-create'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('courses/<int:pk>/update/', CourseUpdateView.as_view(), name='course-update'),
    path('courses/<int:pk>/delete/', CourseDeleteView.as_view(), name='course-delete'),

    # Enrollment URLs
    path('enrollments/', EnrollmentListView.as_view(), name='enrollment-list'),
    path('enrollments/create/', EnrollmentCreateView.as_view(), name='enrollment-create'),

    # Instructor URLs
    path('instructors/', InstructorListView.as_view(), name='instructor-list'),
    path('instructors/create/', InstructorCreateView.as_view(), name='instructor-create'),

    # Lecture URLs
    path('lectures/', LectureListView.as_view(), name='lecture-list'),
    path('lectures/create/', LectureCreateView.as_view(), name='lecture-create'),

    # Rating URLs
    path('ratings/', RatingListView.as_view(), name='rating-list'),
    path('ratings/create/', RatingCreateView.as_view(), name='rating-create'),

    # Section URLs
    path('sections/', SectionListView.as_view(), name='section-list'),
    path('sections/create/', SectionCreateView.as_view(), name='section-create'),

    # Tag URLs
    path('tags/', TagListView.as_view(), name='tag-list'),
    path('tags/create/', TagCreateView.as_view(), name='tag-create'),
]
