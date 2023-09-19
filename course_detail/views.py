from django.shortcuts import render

# Create your views here.
from django.db import models

# Create your models here.
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader

from django.http import HttpResponse
from django.template import loader


def course_detail(request):
    context = {
        # Your context data here
    }
    html_template = loader.get_template("course-details/course-details.html")
    # return HttpResponse(html_template.render(context, request))

    return render(request, 'course-details/course-details.html', context)
