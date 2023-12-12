# views.py

from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from .forms import (
    CategoryForm,
    CourseForm,
    EnrollmentForm,
    InstructorForm,
    LectureForm,
    RatingForm,
    SectionForm,
    TagForm,
)
from .models import (
    Category,
    Course,
    Enrollment,
    Instructor,
    Lecture,
    Rating,
    Section,
    Tag,
)

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'course/category/category_form.html'
    success_url = reverse_lazy('category-list')

class CategoryListView(ListView):
    model = Category
    template_name = 'course/category/category_list.html'
    context_object_name = 'all_categories'

class CourseCreateView(CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'course/course_form.html'
    success_url = reverse_lazy('course-list')

class CourseDeleteView(DeleteView):
    template_name = 'course/delete_course.html'
    model = Course
    success_url = reverse_lazy('course-list')

class CourseDetailView(DetailView):
    model = Course
    template_name = 'course/course_detail.html'

    def course_detail(request, course_id):
        course = get_object_or_404(Course, id=course_id)
        return render(request, 'course/course.html', {'course': course})

class CourseListView(ListView):
    model = Course
    template_name = 'course/course_list.html'
    context_object_name = 'all_courses'

    def get_queryset(self):
        return Course.objects.filter(active=True)

class CourseUpdateView(UpdateView):
    template_name = 'course/update-course.html'
    model = Course
    form_class = CourseForm
    success_url = reverse_lazy('course-list')

class EnrollmentCreateView(CreateView):
    model = Enrollment
    form_class = EnrollmentForm
    template_name = 'course/enrollment/enrollment_form.html'
    success_url = reverse_lazy('enrollment-list')

class EnrollmentListView(ListView):
    model = Enrollment
    template_name = 'course/enrollment/enrollment_list.html'
    context_object_name = 'all_enrollments'

class InstructorCreateView(CreateView):
    model = Instructor
    form_class = InstructorForm
    template_name = 'course/instructor/instructor_form.html'
    success_url = reverse_lazy('instructor-list')

class InstructorListView(ListView):
    model = Instructor
    template_name = 'course/instructor/instructor_list.html'
    context_object_name = 'all_instructors'

class LectureCreateView(CreateView):
    model = Lecture
    form_class = LectureForm
    template_name = 'course/lecture/lecture_form.html'
    success_url = reverse_lazy('lecture-list')

class LectureListView(ListView):
    model = Lecture
    template_name = 'course/lecture/lecture_list.html'
    context_object_name = 'all_lectures'

class RatingCreateView(CreateView):
    model = Rating
    form_class = RatingForm
    template_name = 'course/rating/rating_form.html'
    success_url = reverse_lazy('rating-list')

class RatingListView(ListView):
    model = Rating
    template_name = 'course/rating/rating_list.html'
    context_object_name = 'all_ratings'

class SectionCreateView(CreateView):
    model = Section
    form_class = SectionForm
    template_name = 'course/section/section_form.html'
    success_url = reverse_lazy('section-list')

class SectionListView(ListView):
    model = Section
    template_name = 'course/section/section_list.html'
    context_object_name = 'all_sections'

class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    template_name = 'course/tag/tag_form.html'
    success_url = reverse_lazy('tag-list')

class TagListView(ListView):
    model = Tag
    template_name = 'course/tag/tag_list.html'
    context_object_name = 'all_tags'
