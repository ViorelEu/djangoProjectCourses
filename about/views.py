from django.shortcuts import render, redirect
from .models import About
from .forms import AboutForm
from django.shortcuts import render
from django.template import loader


def about(request):
    context = {
        # Your context data here
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