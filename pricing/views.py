from django.shortcuts import render, redirect
from courses.models import Course  # Import the Course model
from pricing.models import Subscription  # Import the Subscription model
from django.template import loader

# def pricing(request):
#     context = {
#         # Your context data here
#     }
#     html_template = loader.get_template("pricing/pricing.html")
#     # return HttpResponse(html_template.render(context, request))
#
#     return render(request, 'pricing/pricing.html', context)


# defineste clasa in care extindem functionalitatea cursurilor sa abia relatie de many to many cu suubscriptia


# def associate_subscription(request, course_id):
#     course = Course.objects.get(pk=course_id)
#     subscriptions = Subscription.objects.all()  # Get all available subscriptions
#
#     if request.method == 'POST':
#         selected_subscription_ids = request.POST.getlist('subscriptions')  # Get selected subscriptions from the form
#         selected_subscriptions = Subscription.objects.filter(pk__in=selected_subscription_ids)
#         course.subscriptions.set(selected_subscriptions)  # Associate selected subscriptions with the course
#         return redirect('course-detail', pk=course_id)
#
#     context = {
#         'course': course,
#         'subscriptions': subscriptions,
#     }
#
#     return render(request, 'pricing/associate_subscription.html', context)
from django.shortcuts import render, redirect
from courses.models import Course  # Import the Course model
from pricing.models import Subscription  # Import the Subscription model


def pricing(request):
    subscriptions = Subscription.objects.all()
    context = {
        'subscriptions': subscriptions,
    }
    return render(request, 'pricing/pricing.html', context)


def associate_subscription(request, course_id):
    course = Course.objects.get(pk=course_id)
    subscriptions = Subscription.objects.all()

    if request.method == 'POST':
        selected_subscription_ids = request.POST.getlist('subscriptions')
        selected_subscriptions = Subscription.objects.filter(pk__in=selected_subscription_ids)
        course.subscriptions.add(selected_subscriptions)
        return redirect('course-detail', pk=course_id)

    context = {
        'course': course,
        'subscriptions': subscriptions,
    }

    return render(request, 'pricing/associate_subscription.html', context)
