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

from courses.models import Course
from events.models import Event
from student.models import Student
from trainer.models import Trainer
def index(request):
    student_count = Student.objects.count()
    course_count = Course.objects.count()
    event_count = Event.objects.count()
    trainer_count = Trainer.objects.count()

    context = {
        'student_count': student_count,
        'course_count': course_count,
        'event_count': event_count,
        'trainer_count': trainer_count,
    }
    html_template = loader.get_template("home/index.html")
    # return HttpResponse(html_template.render(context, request))

    return render(request, 'home/index.html', context)
