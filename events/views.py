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


def events(request):
    context = {
        # Your context data here
    }
    html_template = loader.get_template("home/events.html")
    # return HttpResponse(html_template.render(context, request))

    return render(request, 'home/events.html', context)
