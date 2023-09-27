from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect

# Create your views here.
from django.db import models

# Create your models here.
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.datetime_safe import datetime

from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

import courses
from .models import Course
from .forms import CourseForm
from django.template import loader


def course(request):
    context = {
        # Your context data here
    }
    html_template = loader.get_template("course/course.html")
    # return HttpResponse(html_template.render(context, request))

    return render(request, 'course/course.html', context)


class CourseCreateView(CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'course/course_form.html'
    success_url = reverse_lazy('courses')
    def form_valid(self, form):
        if form.is_valid():
            new_course = form.save(commit=False)
            new_course.name = new_course.title
            new_course.save()
            return redirect('index')


class CourseListView(ListView):
    model = Course
    template_name = 'course/course.html'
    context_object_name = 'all_courses'
    def get_queryset(self):
        return Course.objects.filter(active=True)

class CourseUpdateView(UpdateView):
    template_name = 'course/update-course.html'
    model = Course
    form_class = CourseForm
    success_url = reverse_lazy('course-list')


class CourseDeleteView(DeleteView):
    template_name = 'course/delete_course.html'
    model = Course
    success_url = reverse_lazy('course-list')


class CourseDetailView(DetailView):
    model = Course
    template_name = 'course/course_detail.html'

# @login_required()
# def search(request):
#     get_value = request.GET.get('filter')
#     if get_value:
#         course = Course.objects.filter(Q(last_name__icontains=get_value) | Q(first_name__icontains=get_value))
#     else:
#         course = course.objects.all()
#
#     return render(request, 'course/course.html', {'all_courses': course})
#
#




