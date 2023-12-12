from django.shortcuts import render, redirect
from .models import About
from .forms import AboutForm
from django.shortcuts import render
from django.template import loader
from courses.models import Course
from events.models import Event
from student.models import Student
from trainer.models import Trainer


def about(request):
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
    html_template = loader.get_template("about/about.html")
    # return HttpResponse(html_template.render(context, request))

    return render(request, 'about/about.html', context)

def edit_about(request):
    about_info = About.objects.first()
    if request.method == 'POST':
        form = AboutForm(request.POST, instance=about_info)
        if form.is_valid():
            form.save()
            return redirect('about')
    else:
        form = AboutForm(instance=about_info)
    return render(request, 'about/edit_about.html', {'form': form})